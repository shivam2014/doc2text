from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import magic
import PyPDF2
import markdown2
from datetime import datetime
import logging
import tempfile
import time
from functools import wraps
import re
import html
import uuid
import subprocess
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("document_converter.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("document_converter")

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Configure CORS

# Constants
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'odt', 'md', 'txt'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# Metrics
request_count = 0
error_count = 0
processing_times = {}

class ConversionError(Exception):
    """Exception raised for errors during document conversion"""
    pass

class ValidationError(Exception):
    """Exception raised for errors during file validation"""
    pass

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def verify_file_type(file_path, expected_type):
    """Verify the actual file type using libmagic"""
    mime = magic.Magic(mime=True)
    file_mime = mime.from_file(file_path)
    
    # Map expected types to MIME types
    mime_map = {
        'pdf': 'application/pdf',
        'doc': 'application/msword',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'odt': 'application/vnd.oasis.opendocument.text',
        'txt': 'text/plain',
        'md': 'text/plain'
    }
    
    if expected_type in mime_map and not file_mime.startswith(mime_map[expected_type]):
        raise ValidationError(f"File type mismatch. Expected {expected_type} but got {file_mime}")

def monitor_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global request_count, error_count
        request_id = str(uuid.uuid4())
        start_time = time.time()
        request_count += 1
        
        logger.info(f"Request {request_id} started")
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            processing_time = end_time - start_time
            processing_times[request_id] = processing_time
            logger.info(f"Request {request_id} completed in {processing_time:.2f}s")
            return result
        except Exception as e:
            error_count += 1
            logger.error(f"Request {request_id} failed: {str(e)}")
            raise
    return wrapper

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'details': {
            'request_count': request_count,
            'error_count': error_count,
            'uptime': time.time() - app.start_time if hasattr(app, 'start_time') else 0
        }
    }), 200

class DocumentConverter:
    @staticmethod
    def sanitize_text(text):
        """Sanitize text to prevent XSS and other attacks while preserving readability"""
        text = re.sub(r'<[^>]*>', lambda m: html.escape(m.group(0)), text)
        text = re.sub(r'javascript:', '', text, flags=re.IGNORECASE)
        text = text.replace('"', '"').replace('&amp;', '&')
        return text

    @staticmethod
    def convert_pdf(file_path):
        try:
            text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    extracted_text = page.extract_text()
                    if extracted_text:
                        text += extracted_text + "\n\n"
                    else:
                        logger.warning(f"Could not extract text from page in {file_path}")
            
            if not text.strip():
                raise ConversionError("Could not extract any text from the PDF file")
                
            return DocumentConverter.sanitize_text(text)
        except Exception as e:
            logger.error(f"Error converting PDF: {str(e)}")
            raise ConversionError(f"Failed to convert PDF: {str(e)}")

    @staticmethod
    def convert_txt(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                return DocumentConverter.sanitize_text(file.read())
        except Exception as e:
            logger.error(f"Error converting TXT: {str(e)}")
            raise ConversionError(f"Failed to convert TXT: {str(e)}")

    @staticmethod
    def convert_md(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                md_content = file.read()
                html_content = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables"])
                text = re.sub(r'<[^>]+>', ' ', html_content)
                text = re.sub(r'\s+', ' ', text)
                return DocumentConverter.sanitize_text(text)
        except Exception as e:
            logger.error(f"Error converting MD: {str(e)}")
            raise ConversionError(f"Failed to convert Markdown: {str(e)}")

    @staticmethod
    def convert_doc(file_path):
        """Convert DOC/DOCX/ODT files using textract"""
        try:
            import textract
            text = textract.process(file_path).decode('utf-8')
            if not text.strip():
                raise ConversionError("Could not extract any text from the document")
            return DocumentConverter.sanitize_text(text)
        except Exception as e:
            logger.error(f"Error converting document: {str(e)}")
            raise ConversionError(f"Failed to convert document: {str(e)}")

@app.route('/api/v1/convert', methods=['POST'])
@monitor_performance
def convert_document():
    temp_path = None
    try:
        if 'file' not in request.files:
            logger.warning("No file provided in request")
            return jsonify({
                'status': 'error',
                'error': 'No file provided'
            }), 400

        file = request.files['file']
        if file.filename == '':
            logger.warning("Empty filename provided")
            return jsonify({
                'status': 'error',
                'error': 'No selected file'
            }), 400

        # Check file size
        file.seek(0, 2)  # Seek to end of file
        file_size = file.tell()
        file.seek(0)  # Reset file pointer
        
        if file_size > MAX_FILE_SIZE:
            logger.warning(f"File size {file_size} exceeds maximum allowed size {MAX_FILE_SIZE}")
            return jsonify({
                'status': 'error',
                'error': f'File size exceeds maximum allowed size of {MAX_FILE_SIZE//(1024*1024)}MB'
            }), 400

        if not allowed_file(file.filename):
            logger.warning(f"Unsupported file type: {file.filename}")
            return jsonify({
                'status': 'error',
                'error': 'File type not supported. Allowed types are PDF, DOC, DOCX, ODT, MD, and TXT'
            }), 400

        filename = secure_filename(file.filename)
        
        # Create temp file
        temp_fd, temp_path = tempfile.mkstemp()
        os.close(temp_fd)
        file.save(temp_path)

        # Verify file type
        file_type = filename.rsplit('.', 1)[1].lower()
        try:
            verify_file_type(temp_path, file_type)
        except ValidationError as e:
            logger.warning(f"File type validation failed: {str(e)}")
            return jsonify({
                'status': 'error',
                'error': str(e)
            }), 400

        # Convert based on file type
        converter = DocumentConverter()
        conversion_method = {
            'pdf': converter.convert_pdf,
            'doc': converter.convert_doc,
            'docx': converter.convert_doc,
            'odt': converter.convert_doc,
            'txt': converter.convert_txt,
            'md': converter.convert_md
        }

        converted_text = conversion_method[file_type](temp_path)
        
        logger.info(f"Successfully converted {filename}")
        
        return jsonify({
            'status': 'success',
            'data': {
                'text': converted_text,
                'metadata': {
                    'original_filename': filename,
                    'file_type': file_type,
                    'conversion_time': datetime.utcnow().isoformat(),
                    'text_length': len(converted_text)
                }
            }
        }), 200

    except ConversionError as e:
        logger.error(f"Conversion error: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 422
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({
            'status': 'error',
            'error': 'An unexpected error occurred during processing'
        }), 500
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

# Set app start time
app.start_time = time.time()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

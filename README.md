# Document Converter API

A Flask-based API service that converts various document formats into text while preserving document structure. Uses PyMuPDF4LLM for enhanced PDF conversion with markdown output. Supports PDF, DOC, DOCX, ODT, Markdown, and plain text files.

## Installation

### Prerequisites
- Python 3.8 or higher
- uv package manager
- PyMuPDF4LLM for enhanced PDF text extraction
- python-magic-bin for file type validation (Windows only)
- textract for Word document conversion

## Document Conversion

The application now uses PyMuPDF4LLM for PDF processing, which offers several advantages:

- Improved document structure preservation
- Better handling of multi-column layouts
- Support for tables and lists
- Markdown-formatted output
- Enhanced text extraction quality

### Dependencies

- `pymupdf4llm`: PDF processing and text extraction
- `flask`: Web framework
- `flask-cors`: Cross-origin resource sharing
- `markdown2`: Markdown processing
- `python-magic`: File type detection
- `textract`: Document format conversion
- `reportlab`: PDF creation (testing only)

### Features
- Enhanced PDF text extraction with preserved document structure
- Markdown-formatted output for PDFs
- Robust file handle management with automatic cleanup
- Automatic retry mechanism for file operations
- Content sanitization and XSS prevention

### Setup Virtual Environment

#### Windows (PowerShell)
```powershell
# Create virtual environment
uv venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
uv pip install -r app/requirements.txt
```

#### Windows (Command Prompt)
```cmd
# Create virtual environment
uv venv

# Activate virtual environment
.\.venv\Scripts\activate.bat

# Install dependencies
uv pip install -r app/requirements.txt
```

#### macOS/Linux
```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv pip install -r app/requirements.txt
```

## Running the API Server

Once the environment is set up, you can start the Flask server:

```bash
uv run flask --app app.api.document_converter run
```

The server will start on `http://localhost:5000` by default.

## Using the Demo Script

A demo script (`demo.py`) is provided to easily test the document conversion functionality.

### Usage
```bash
python demo.py /path/to/your/file.<extension>
```

### Examples
```bash
# Convert a PDF file
python demo.py tests/test_files/sample.pdf

# Convert a text file
python demo.py tests/test_files/sample.txt

# Convert a markdown file
python demo.py tests/test_files/sample.md
```

### Supported File Types
- PDF (.pdf)
- Microsoft Word (.doc, .docx)
- OpenDocument Text (.odt)
- Markdown (.md)
- Text (.txt)

## API Endpoints

### Convert Document
- **URL**: `/api/v1/convert`
- **Method**: `POST`
- **Content-Type**: `multipart/form-data`
- **Form Parameters**:
  - `file`: The document file to convert

#### Success Response
```json
{
    "status": "success",
    "data": {
        "text": "# Document Title\n\nExtracted content with preserved structure...",
        "metadata": {
            "original_filename": "example.pdf",
            "file_type": "pdf",
            "conversion_time": "2024-03-25T20:00:00.000Z",
            "text_length": 1234
        }
    }
}
```

#### Error Response
```json
{
    "status": "error",
    "error": "Error message description"
}
```

### Health Check
- **URL**: `/api/v1/health`
- **Method**: `GET`

#### Response
```json
{
    "status": "healthy",
    "details": {
        "request_count": 42,
        "error_count": 0,
        "uptime": 3600
    }
}
```

## Limitations
- Maximum file size: 10MB
- PDF files must be text-based (scanned PDFs require OCR, which is not supported)
- PDF output is converted to markdown format for better structure preservation
- Word documents (.doc, .docx) require `textract` package with proper system dependencies
- PDF processing may require additional system memory for large documents
- File cleanup may require multiple attempts on Windows systems due to file locking

## Development

### Running Tests
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_document_converter.py -v

# Run with sample files
python demo.py tests/test_files/sample.pdf  # Test PDF conversion
python demo.py tests/test_files/sample.txt  # Test text conversion
python demo.py tests/test_files/sample.md   # Test markdown conversion
```

Note: Sample files are provided in the tests/test_files directory for testing different conversion scenarios. The PDF conversion will output markdown-formatted text that preserves the document's structure.

### Logging
Logs are written to `document_converter.log` in the project directory.

## Security Notes
- File types are validated both by extension and MIME type
- Text content is sanitized to prevent XSS attacks
- CORS is enabled for all origins (customize in production)
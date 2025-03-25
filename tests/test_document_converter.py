import unittest
import os
import json
import tempfile
import os
import sys

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.api.document_converter import app, DocumentConverter

class DocumentConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        # Create test files
        self.test_files = {}
        
        # Create a test PDF file
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
            # Write a simple PDF content
            f.write(b'%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Count 1 /Kids [3 0 R] >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Contents 4 0 R >>\nendobj\n4 0 obj\n<< >>\nstream\nBT\n/F1 12 Tf\n72 712 Td\n(Test PDF Content) Tj\nET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f\n0000000009 00000 n\n0000000058 00000 n\n0000000115 00000 n\n0000000174 00000 n\ntrailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n270\n%%EOF\n')
            self.test_files['pdf'] = f.name
        
        # Create a test txt file
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
            f.write(b'This is a test text file.\nWith multiple lines.')
            self.test_files['txt'] = f.name
            
        # Create a test markdown file
        with tempfile.NamedTemporaryFile(suffix='.md', delete=False) as f:
            f.write(b'# Test Markdown\n\nThis is a **test** markdown file.')
            self.test_files['md'] = f.name
            
        # Create a test LaTeX file
        with tempfile.NamedTemporaryFile(suffix='.tex', delete=False) as f:
            f.write(b'\\documentclass{article}\n\\begin{document}\nThis is a test LaTeX file.\n\\end{document}')
            self.test_files['tex'] = f.name
    
    def tearDown(self):
        # Clean up test files
        for file_path in self.test_files.values():
            if os.path.exists(file_path):
                os.remove(file_path)
    
    def test_health_endpoint(self):
        response = self.app.get('/api/v1/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        
    def test_convert_txt(self):
        with open(self.test_files['txt'], 'rb') as f:
            response = self.app.post(
                '/api/v1/convert',
                data={'file': (f, 'test.txt')},
                content_type='multipart/form-data'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['status'], 'success')
            self.assertIn('This is a test text file', data['data']['text'])
    
    def test_convert_pdf(self):
        """Test PDF conversion using PyMuPDF4LLM"""
        with open(self.test_files['pdf'], 'rb') as f:
            response = self.app.post(
                '/api/v1/convert',
                data={'file': (f, 'sample.pdf')},
                content_type='multipart/form-data'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['status'], 'success')
            
            # Check for expected content in the converted text
            self.assertIn('Test PDF Content', data['data']['text'])
            # Verify markdown formatting markers
            self.assertIn('-----', data['data']['text'])  # PyMuPDF4LLM adds horizontal rules
            
            # Verify metadata
            self.assertEqual(data['data']['metadata']['file_type'], 'pdf')
            self.assertTrue(len(data['data']['text']) > 0)
    
    def test_convert_pdf_invalid(self):
        """Test PDF conversion with invalid file"""
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
            f.write(b'This is not a valid PDF file')
            f.flush()
            
            with open(f.name, 'rb') as invalid_pdf:
                response = self.app.post(
                    '/api/v1/convert',
                    data={'file': (invalid_pdf, 'invalid.pdf')},
                    content_type='multipart/form-data'
                )
                self.assertEqual(response.status_code, 400)
                data = json.loads(response.data)
                self.assertEqual(data['status'], 'error')
                self.assertIn('File type mismatch', data['error'])
    
    def test_file_too_large(self):
        """Test file size limit enforcement"""
        # Create a large temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        try:
            # Write content larger than MAX_FILE_SIZE (10MB + 1 byte)
            temp_file.write(b'x' * (10 * 1024 * 1024 + 1))
            temp_file.flush()
            temp_file.close()
            
            with open(temp_file.name, 'rb') as large_file:
                response = self.app.post(
                    '/api/v1/convert',
                    data={'file': (large_file, 'large.txt')},
                    content_type='multipart/form-data'
                )
                self.assertEqual(response.status_code, 400)
                data = json.loads(response.data)
                self.assertEqual(data['status'], 'error')
                self.assertIn('size exceeds', data['error'])
        finally:
            # Clean up in finally block to ensure it happens
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)

if __name__ == '__main__':
    unittest.main()

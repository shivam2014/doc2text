import unittest
import os
import json
import tempfile
import sys
sys.path.append('../app')
from api.document_converter import app, DocumentConverter

class DocumentConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        # Create test files
        self.test_files = {}
        
        # Create a test PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
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
    
    # Add more tests for other file types
    
    def test_file_too_large(self):
        # Mock a file that exceeds the size limit
        app.config['MAX_FILE_SIZE'] = 10  # Temporarily set max size to 10 bytes
        with open(self.test_files['txt'], 'rb') as f:
            response = self.app.post(
                '/api/v1/convert',
                data={'file': (f, 'test.txt')},
                content_type='multipart/form-data'
            )
            self.assertEqual(response.status_code, 400)
            data = json.loads(response.data)
            self.assertEqual(data['status'], 'error')
            self.assertIn('size exceeds', data['error'])
        app.config['MAX_FILE_SIZE'] = 10 * 1024 * 1024  # Reset to original

if __name__ == '__main__':
    unittest.main()

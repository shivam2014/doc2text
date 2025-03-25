import pytest
import requests
import os
import tempfile
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@pytest.fixture
def test_files():
    """Fixture that creates test files of different formats"""
    files = {}
    
    # Create test text file
    txt_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
    txt_file.write(b'This is a test text file.\nWith multiple lines.')
    txt_file.close()
    files['txt'] = txt_file.name
    
    # Create test markdown file
    md_file = tempfile.NamedTemporaryFile(suffix='.md', delete=False)
    md_file.write(b'# Test Markdown\n\nThis is a **test** markdown file.')
    md_file.close()
    files['md'] = md_file.name
    
    yield files
    
    # Cleanup
    for file_path in files.values():
        if os.path.exists(file_path):
            os.remove(file_path)

def test_conversion_txt(test_files):
    """Test text file conversion"""
    base_url = 'http://localhost:5000/api/v1'
    with open(test_files['txt'], 'rb') as f:
        response = requests.post(f'{base_url}/convert', files={'file': f})
    
    assert response.status_code == 200
    result = response.json()
    assert result['status'] == 'success'
    assert 'This is a test text file' in result['data']['text']

def test_conversion_md(test_files):
    """Test markdown file conversion"""
    base_url = 'http://localhost:5000/api/v1'
    with open(test_files['md'], 'rb') as f:
        response = requests.post(f'{base_url}/convert', files={'file': f})
    
    assert response.status_code == 200
    result = response.json()
    assert result['status'] == 'success'
    assert 'Test Markdown' in result['data']['text']

def test_unsupported_format(tmp_path):
    """Test unsupported file format"""
    base_url = 'http://localhost:5000/api/v1'
    unsupported_file = tmp_path / "test.unsupported"
    unsupported_file.write_text("Test content")
    
    with open(unsupported_file, 'rb') as f:
        response = requests.post(f'{base_url}/convert', files={'file': f})
    
    assert response.status_code == 400
    result = response.json()
    assert result['status'] == 'error'
    assert 'File type not supported' in result['error']

import pytest
import requests
import os
import tempfile
import logging
from pathlib import Path
from reportlab.pdfgen import canvas

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
    
    # Create test PDF file with some structure
    pdf_file = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
    pdf_file.close()
    
    # Use a sample PDF from test_files directory
    sample_pdf = Path(__file__).parent / 'test_files' / 'sample.pdf'
    if sample_pdf.exists():
        import shutil
        shutil.copy(sample_pdf, pdf_file.name)
    else:
        # Create a simple PDF if sample doesn't exist
        c = canvas.Canvas(pdf_file.name)
        c.drawString(100, 750, "# Test PDF Document")
        c.drawString(100, 700, "This is a test PDF file.")
        c.drawString(100, 650, "* List item 1")
        c.drawString(100, 630, "* List item 2")
        c.save()
    
    files['pdf'] = pdf_file.name
    
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

def test_conversion_pdf(test_files):
    """Test PDF file conversion with PyMuPDF4LLM"""
    base_url = 'http://localhost:5000/api/v1'
    with open(test_files['pdf'], 'rb') as f:
        response = requests.post(f'{base_url}/convert', files={'file': f})
    
    assert response.status_code == 200
    result = response.json()
    assert result['status'] == 'success'
    
    # Check if markdown structure is preserved
    text = result['data']['text']
    assert '#' in text  # Should contain headers
    assert text.strip()  # Should not be empty
    
    # Log the converted text for inspection
    logger.info(f"Converted PDF text preview:\n{text[:500]}")

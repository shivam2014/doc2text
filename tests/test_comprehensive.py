import pytest
import requests
import os
import time
import tempfile
import logging
from pathlib import Path
from typing import Dict, Any
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

BASE_URL = 'http://localhost:5000/api/v1'
TEST_FILES_DIR = Path('tests/test_files')

def get_file_size(file_path: str) -> int:
    """Get file size in bytes"""
    return os.path.getsize(file_path)

def measure_performance(file_path: str) -> Dict[str, float]:
    """Measure conversion performance for a single file"""
    start_time = time.time()
    with open(file_path, 'rb') as f:
        response = requests.post(f'{BASE_URL}/convert', files={'file': f})
    end_time = time.time()
    
    return {
        'time': end_time - start_time,
        'size': get_file_size(file_path),
        'status': response.status_code
    }

@pytest.fixture
def test_files() -> Dict[str, str]:
    """Fixture providing paths to test files"""
    files = {}
    
    # Use existing test files
    files['pdf'] = str(TEST_FILES_DIR / 'Default_Resume-template.pdf')
    files['md'] = str(TEST_FILES_DIR / 'sample.md')
    files['txt'] = str(TEST_FILES_DIR / 'sample.txt')
    
    # Create additional test files
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
        f.write(b'')  # Empty file
        files['empty'] = f.name
        
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as f:
        f.write(b'Mock DOCX content')  # Unsupported format
        files['unsupported'] = f.name
        
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
        f.write(b'<script>alert("XSS")</script>')  # Unsafe content
        files['unsafe'] = f.name
        
    yield files
    
    # Cleanup temporary files
    for key in ['empty', 'unsupported', 'unsafe']:
        if os.path.exists(files[key]):
            os.remove(files[key])

def test_supported_formats(test_files: Dict[str, str]):
    """Test conversion of all supported formats"""
    supported_files = ['pdf', 'md', 'txt']
    
    for fmt in supported_files:
        logger.info(f"Testing {fmt.upper()} conversion")
        with open(test_files[fmt], 'rb') as f:
            response = requests.post(f'{BASE_URL}/convert', files={'file': f})
        
        assert response.status_code == 200
        result = response.json()
        assert result['status'] == 'success'
        assert isinstance(result['data']['text'], str)
        assert len(result['data']['text']) > 0
        
        # Basic content quality checks
        text = result['data']['text'].lower()
        assert not any(marker in text for marker in ['error', 'exception', 'failed'])
        assert text.strip() != ''
        assert len(text.split()) > 5  # Should have more than 5 words

def test_error_handling(test_files: Dict[str, str]):
    """Test various error conditions"""
    
    # Test empty file
    with open(test_files['empty'], 'rb') as f:
        response = requests.post(f'{BASE_URL}/convert', files={'file': f})
    assert response.status_code == 400
    assert response.json()['status'] == 'error'
    
    # Test unsupported file type
    with open(test_files['unsupported'], 'rb') as f:
        response = requests.post(f'{BASE_URL}/convert', files={'file': f})
    assert response.status_code == 400
    assert 'mismatch' in response.json()['error'].lower()
    
    # Test missing file
    response = requests.post(f'{BASE_URL}/convert')
    assert response.status_code == 400
    assert 'file' in response.json()['error'].lower()
    
    # Test malformed request
    response = requests.post(f'{BASE_URL}/convert', data='not a file')
    assert response.status_code == 400

def test_unsafe_content(test_files: Dict[str, str]):
    """Test handling of potentially unsafe content in text files"""
    with open(test_files['unsafe'], 'rb') as f:
        response = requests.post(f'{BASE_URL}/convert', files={'file': f})
    
    # Server should accept the file but sanitize the content
    if response.status_code == 200:
        result = response.json()
        assert result['status'] == 'success'
        # Check that unsafe content is properly handled
        assert '<script>' not in result['data']['text'].lower()
        assert 'alert' not in result['data']['text'].lower()
    else:
        # Or reject it with a 400 if that's the security policy
        assert response.status_code == 400
        assert response.json()['status'] == 'error'

def test_response_format():
    """Test API response format and structure"""
    with open(TEST_FILES_DIR / 'sample.txt', 'rb') as f:
        response = requests.post(f'{BASE_URL}/convert', files={'file': f})
    
    assert response.status_code == 200
    result = response.json()
    
    # Check response structure
    assert isinstance(result, dict)
    assert 'status' in result
    assert 'data' in result
    assert 'text' in result['data']
    assert isinstance(result['data']['text'], str)
    
    # Check additional metadata if present
    if 'metadata' in result['data']:
        assert isinstance(result['data']['metadata'], dict)

def test_conversion_performance():
    """Test conversion performance for different file types"""
    results = {}
    
    # Test each supported format
    test_files = {
        'pdf': TEST_FILES_DIR / 'Default_Resume-template.pdf',
        'md': TEST_FILES_DIR / 'sample.md',
        'txt': TEST_FILES_DIR / 'sample.txt'
    }
    
    for fmt, file_path in test_files.items():
        # Run multiple iterations
        iterations = 3
        timings = []
        
        for _ in range(iterations):
            result = measure_performance(str(file_path))
            if result['status'] == 200:
                timings.append(result['time'])
        
        if timings:
            results[fmt] = {
                'mean_time': sum(timings) / len(timings),
                'min_time': min(timings),
                'max_time': max(timings),
                'file_size': result['size']
            }
            
            # Log performance metrics
            logger.info(
                f"\n{fmt.upper()} Conversion Metrics:\n"
                f"File size: {result['size']/1024:.2f}KB\n"
                f"Mean time: {results[fmt]['mean_time']:.3f}s\n"
                f"Min time: {results[fmt]['min_time']:.3f}s\n"
                f"Max time: {results[fmt]['max_time']:.3f}s"
            )
            
            # Basic performance assertions
            assert results[fmt]['mean_time'] < 10.0, f"Conversion time for {fmt} too slow"

def test_concurrent_requests(test_files: Dict[str, str]):
    """Test handling of concurrent requests"""
    import concurrent.futures
    
    def make_request(file_path: str) -> bool:
        with open(file_path, 'rb') as f:
            response = requests.post(f'{BASE_URL}/convert', files={'file': f})
        return response.status_code == 200
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(make_request, test_files['txt'])
            for _ in range(3)
        ]
        results = [future.result() for future in futures]
    
    assert all(results)  # All requests should succeed

if __name__ == '__main__':
    pytest.main(['-v', __file__])
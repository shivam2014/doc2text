# Document Converter API

A Flask-based API service that converts various document formats into plain text. Supports PDF, DOC, DOCX, ODT, Markdown, and plain text files.

## Installation

### Prerequisites
- Python 3.8 or higher
- uv package manager

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
        "text": "extracted text content...",
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
- Word documents (.doc, .docx) require `textract` package with proper system dependencies

## Development

### Running Tests
```bash
pytest tests/
```

### Logging
Logs are written to `document_converter.log` in the project directory.

## Security Notes
- File types are validated both by extension and MIME type
- Text content is sanitized to prevent XSS attacks
- CORS is enabled for all origins (customize in production)
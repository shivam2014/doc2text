# Document Converter API Deployment Guide

## Prerequisites
- Python 3.8+
- pandoc (for LaTeX conversion)
- libmagic (for file type detection)

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd latex2text
```

### 2. Install Dependencies
```bash
pip install -r app/requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory:
```
FLASK_ENV=production
CORS_ALLOWED_ORIGINS=https://yourdomain.com
LOG_LEVEL=INFO
```

### 4. Run with Gunicorn (Production)
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 app.api.document_converter:app
```

## Docker Deployment

### 1. Build the Docker Image
```bash
docker build -t document-converter-api .
```

### 2. Run the Container
```bash
docker run -d -p 5000:5000 --env-file .env --name document-converter document-converter-api
```

## Monitoring

### Health Check
The API provides a health check endpoint at `/api/v1/health` that returns basic metrics:
- Request count
- Error count
- Average processing time

### Logging
Logs are written to `document_converter.log` and also output to stdout.

## Security Considerations

### File Size Limits
Maximum file size is 10MB.

## Performance Tuning

For high-traffic deployments:
- Increase the number of Gunicorn workers (2-4× the number of CPU cores)
- Consider using a reverse proxy like Nginx
- Implement caching for frequently accessed documents

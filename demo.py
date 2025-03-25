#!/usr/bin/env python3
"""
Document Converter Demo Script

This script demonstrates the usage of the Document Converter API by sending files
for text extraction. It supports various file formats including PDF, DOC, DOCX,
ODT, Markdown, and plain text files.

Usage:
    python demo.py /path/to/your/file.pdf
    python demo.py /path/to/your/file.txt
    python demo.py /path/to/your/file.md

Make sure the Flask API server is running before using this script:
    uv run flask --app app.api.document_converter run
"""

import requests
import argparse
import sys
import os
from pathlib import Path

def convert_document(file_path: str) -> None:
    """
    Send a document to the converter API and display the extracted text.

    Args:
        file_path (str): Path to the document file to be converted.
            Supported formats: PDF, DOC, DOCX, ODT, MD, TXT

    Raises:
        SystemExit: If the file doesn't exist, has unsupported type,
                   or if API communication fails.
    
    Example:
        >>> convert_document("example.pdf")
        Extracted Text:
        ----------------
        [Extracted content will be displayed here]
        ----------------
        Metadata:
        Original filename: example.pdf
        File type: pdf
        ...
    """
    # Validate file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist")
        sys.exit(1)

    # Get file extension
    extension = Path(file_path).suffix.lower()[1:]  # Remove the dot
    allowed_extensions = {'pdf', 'doc', 'docx', 'odt', 'md', 'txt'}
    
    if extension not in allowed_extensions:
        print(f"Error: Unsupported file type '{extension}'. Supported types are: {', '.join(allowed_extensions)}")
        sys.exit(1)

    # API endpoint
    url = 'http://localhost:5000/api/v1/convert'
    
    try:
        # Open and send the file
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f)}
            response = requests.post(url, files=files)

        # Check response
        response.raise_for_status()
        result = response.json()

        if result['status'] == 'success':
            # Print the extracted text
            print("\nExtracted Text:")
            print("-" * 80)
            print(result['data']['text'])
            print("-" * 80)
            
            # Print metadata
            metadata = result['data']['metadata']
            print("\nMetadata:")
            print(f"Original filename: {metadata['original_filename']}")
            print(f"File type: {metadata['file_type']}")
            print(f"Conversion time: {metadata['conversion_time']}")
            print(f"Text length: {metadata['text_length']} characters")
        else:
            print(f"Error: {result.get('error', 'Unknown error occurred')}")
            sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API server. Make sure it's running with:")
        print("  uv run flask --app app.api.document_converter run")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    """
    Main entry point for the document converter demo script.
    Parses command line arguments and initiates the conversion process.
    """
    parser = argparse.ArgumentParser(
        description='Convert documents to text using the document converter API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('file_path', help='Path to the file to convert')
    
    args = parser.parse_args()
    convert_document(args.file_path)

if __name__ == '__main__':
    main()
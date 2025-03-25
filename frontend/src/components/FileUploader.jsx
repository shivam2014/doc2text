import { useState } from 'react';

const FileUploader = ({ onTextReceived }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [progress, setProgress] = useState(0);
  
  const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api/v1/convert';
  
  const validateFile = (file) => {
    const allowedTypes = ['application/pdf', 'text/plain', 'text/markdown', 'application/x-tex'];
    const maxSize = 10 * 1024 * 1024; // 10MB
    
    if (!allowedTypes.includes(file.type) && 
        !file.name.endsWith('.md') && 
        !file.name.endsWith('.tex')) {
      throw new Error('File type not supported. Please upload PDF, TXT, MD, or TEX files.');
    }
    
    if (file.size > maxSize) {
      throw new Error('File size exceeds 10MB limit.');
    }
    
    return true;
  };

  const uploadFile = async (file) => {
    setIsLoading(true);
    setError(null);
    setProgress(0);
    
    try {
      // Validate file before uploading
      validateFile(file);
      
      const formData = new FormData();
      formData.append('file', file);
      
      const xhr = new XMLHttpRequest();
      
      // Set up progress monitoring
      xhr.upload.addEventListener('progress', (event) => {
        if (event.lengthComputable) {
          const percentComplete = Math.round((event.loaded / event.total) * 100);
          setProgress(percentComplete);
        }
      });
      
      // Create a promise to handle the XHR request
      const response = await new Promise((resolve, reject) => {
        xhr.open('POST', API_URL);
        
        xhr.onload = () => {
          if (xhr.status >= 200 && xhr.status < 300) {
            resolve(JSON.parse(xhr.responseText));
          } else {
            try {
              const errorData = JSON.parse(xhr.responseText);
              reject(new Error(errorData.error || 'Upload failed'));
            } catch (e) {
              reject(new Error(`Upload failed with status ${xhr.status}`));
            }
          }
        };
        
        xhr.onerror = () => reject(new Error('Network error occurred'));
        xhr.ontimeout = () => reject(new Error('Request timed out'));
        
        xhr.send(formData);
      });
      
      if (response.status === 'success') {
        // Handle the converted text
        onTextReceived && onTextReceived(response.data.text, response.data.metadata);
      } else {
        // This should not typically happen as errors should be caught in the XHR error handler
        throw new Error(response.error || 'Unknown error occurred');
      }
    } catch (error) {
      setError(error.message);
      console.error('Upload failed:', error);
    } finally {
      setIsLoading(false);
      setProgress(0);
    }
  };
  
  return (
    <div className="file-uploader">
      <input 
        type="file" 
        accept=".pdf,.txt,.md,.tex"
        onChange={(e) => {
          if (e.target.files && e.target.files[0]) {
            uploadFile(e.target.files[0]);
          }
        }}
        disabled={isLoading}
      />
      
      {isLoading && (
        <div className="progress-container">
          <div className="progress-bar" style={{ width: `${progress}%` }}></div>
          <span>{progress}%</span>
        </div>
      )}
      
      {error && (
        <div className="error-message">
          Error: {error}
        </div>
      )}
    </div>
  );
};

export default FileUploader;
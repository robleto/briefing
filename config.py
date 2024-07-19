import os

class Config:
    # Email server configuration
    MAIL_SERVER = 'smtp.gmail.com'  # For Gmail
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  # Set this environment variable
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')  # Set this environment variable
    
    # OpenAI API key
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')  # Set this environment variable

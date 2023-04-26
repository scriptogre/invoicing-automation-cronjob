import os

from dotenv import load_dotenv

load_dotenv()

# Factureaza.ro configuration
FACTUREAZA_RO_API_URL = os.environ.get('FACTUREAZA_RO_API_URL')
FACTUREAZA_RO_API_KEY = os.environ.get('FACTUREAZA_RO_API_KEY')

# Outlook configuration
OUTLOOK_HOST = os.environ.get('OUTLOOK_HOST')
OUTLOOK_PORT = os.environ.get('OUTLOOK_PORT')
OUTLOOK_EMAIL = os.environ.get('OUTLOOK_EMAIL')
OUTLOOK_PASSWORD = os.environ.get('OUTLOOK_PASSWORD')

# Mailhog configuration
MAILHOG_HOST = os.environ.get('MAILHOG_HOST')
MAILHOG_PORT = os.environ.get('MAILHOG_PORT')

# Sentry DSN
SENTRY_DSN = os.environ.get('SENTRY_DSN')

# Application configuration
APP_NAME = os.environ.get('APP_NAME')

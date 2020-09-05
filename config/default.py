import os
from os.path import abspath, dirname, join


# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')

SECRET_KEY = os.urandom(32)

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Email configuration
MAIL_SERVER = 'your smtp server'
MAIL_PORT = 587
MAIL_USERNAME = 'your email'
MAIL_PASSWORD = 'your password'
DONT_REPLY_FROM_EMAIL = 'from address'
ADMINS = ('jetro4100@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False

ITEMS_PER_PAGE = 3
ITEMS_PER_LIST = 200

BASE_DIR = 'static'

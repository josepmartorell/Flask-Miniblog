import os

from .default import *


SECRET_KEY = os.urandom(32)

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@host:port/db_name'

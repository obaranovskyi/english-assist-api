"""Flask configuration."""

from os import path, environ
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

SECRET_KEY = environ.get('SECRET_KEY')
FLASK_ENV = 'development'
SQLALCHEMY_DATABASE_URI =\
    'sqlite:///' + path.join(basedir, 'english_assist.db')

"""
author :
date :
purpose :
"""

# future

# standard-library

# third-party
import environ
import  os

# django
from django.core.exceptions import ImproperlyConfigured

# local


ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('apps')

ENV = environ.Env()
ENV_FILE = str(ROOT_DIR.path(".env"))  # reading .env file
ENV.read_env(ENV_FILE)

SECRET_KEY = ENV.str('SECRET_KEY')

DEBUG = ENV.bool('DEBUG', default=False)

PROJECT_HOST = ENV.str('PROJECT_HOST', default='local')
ALLOWED_HOSTS = ENV.list('ALLOWED_HOSTS', default=['localhost'])

ROOT_URLCONF = 'bookstore.urls'

WSGI_APPLICATION = 'bookstore.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ----------------------------------------------------------------------------
# Database
# ----------------------------------------------------------------------------

if PROJECT_HOST == 'local':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': str(ROOT_DIR.path('data/db.sqlite3')),
        }
    }
else:
    try:
        DATABASES = {"default": ENV.db('DB_URL')}
    except ImproperlyConfigured:
        DATABASES = {
            "default":
                {
                    'ENGINE': ENV.str('DB_ENGINE'),
                    'NAME': ENV.str('DB_NAME'),
                    'USER': ENV.str('DB_USER'),
                    'PASSWORD': ENV.str('DB_PASSWORD'),
                    'HOST': ENV.str('DB_HOST'),
                    'PORT': ENV.str('DB_PORT')
                }
        }

# ----------------------------------------------------------------------------
# APPS & MIDDLEWARE
# ----------------------------------------------------------------------------

LOCAL_APPS = (
)

# ----------------------------------------------------------------------------
# others
# ----------------------------------------------------------------------------

DATE_TIME_DISPLAY_FORMAT = "%Y-%m-%d %H:%M:%S %Z"

# -----------------------------------------------------------------------------
# Static
# -----------------------------------------------------------------------------

STATIC_URL = 'static/'

#cache
REDIS_URL = ENV("REDIS_URL")
CACHE_TIMEOUT = int(ENV("CACHE_TIMEOUT", default=600))
ENABLE_CACHE = ENV("ENABLE_CACHE", default=True)
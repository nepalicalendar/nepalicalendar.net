# settings/local.py
import os

from .base import *


DEBUG = False

SECRET_KEY = get_env_variable("SECRET_KEY")

ALLOWED_HOSTS = [
  '.nepalicalendar.net',
  '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticdeploy'

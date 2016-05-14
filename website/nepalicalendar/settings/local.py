# settings/local.py
import os

from .base import *


# INSTALLED_APPS += ("debug_toolbar", )

SECRET_KEY = '*4ymk7---69z_v#ee#c2o440r&31ni_&6xzdtm$s&!(w!qpu-g'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



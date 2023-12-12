'''
author :
date :
purpose :
'''

#future

# standard-library

# third-party

# django
import environ

# local

from .project import *
from .django import *
from .third_party import THIRD_PARTY_APPS, THIRD_PARTY_MIDDLEWARE
from .third_party.cors import *
# from .third_party.ldap import *
# from .third_party.aws import *
from .third_party.drf import *
from .third_party.jwt import *



INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

AUTHENTICATION_BACKENDS = DJANGO_BACKEND

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             # "filename": "/path/to/django/debug.log",
#             "filename": str(ROOT_DIR.path('logs/debug.log')),
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#     },
# }
"""
author :
date :
purpose :
"""

# future

# standard-library

# third-party

# django

# local
from bookstore.settings import ENV

CORS_ORIGIN_WHITELIST = ENV.tuple('CORS_ORIGIN_WHITELIST')
CORS_ORIGIN_ALLOW_ALL = ENV.bool('CORS_ORIGIN_ALLOW_ALL', default=False)

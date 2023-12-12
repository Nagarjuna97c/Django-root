"""
author :
date :
purpose :
"""

# future

# standard-library
import datetime
from datetime import timedelta

# third-party

# django

# local
from bookstore.settings import SECRET_KEY

# -----------------------------------------------------------------------------
# jwt_settings
# -----------------------------------------------------------------------------

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=300000),  # 300 seconds
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=14),
    'SLIDING_TOKEN_REFRESH_LIFETIME_ALLOW_SAMESITE': True,
    'SLIDING_TOKEN_REFRESH_LIFETIME_SAMESITE': 'Lax',
    'SLIDING_TOKEN_LIFETIME_ALLOW_RENEWAL': True,
    'SLIDING_TOKEN_REFRESH_LIFETIME_ALLOW_RENEWAL': True,
    'ROTATE_REFRESH_TOKENS': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer', 'Token', 'TOKEN'),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
}
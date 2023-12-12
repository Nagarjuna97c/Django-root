"""
author :
date :
purpose :
"""

# future

# standard-library
import logging
from datetime import datetime

# third-party

# django

# local
from bookstore.settings import ENV

logger = logging.getLogger(__name__)

logger_level = ENV('LOGGER_LEVEL')

if logger_level.upper() in ('INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'):
    logger.setLevel(getattr(logging, logger_level.upper()))
else:
    logger.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "[ %(process)s %(thread)s %(asctime)s, %(levelname)s, %(module)s, %(funcName)s, %(lineno)d ]: %(message)s",
    "%Y-%m-%d %H:%M:%S",
)
logger.propagate = False

LOG_FILENAME = 'bookstore-server-log' + datetime.now()
LOG_FILEPATH = 'logs/' + LOG_FILENAME

file_handler = logging.handlers.TimedRotatingFileHandler(LOG_FILEPATH, when='midnight', backupCount=7)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
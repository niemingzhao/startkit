# -*- coding: utf-8 -*-

import logging
import logging.config

logging.config.dictConfig({
    'version': 1,
    'root': {
        'level': logging.DEBUG,
        'handlers': ['console_handler', 'application_handler']
    },
    'handlers': {
        'console_handler': {  # Handler to Console
            'class': 'logging.StreamHandler',
            'level': logging.DEBUG,
            'formatter': 'formatter'
        },
        'library_handler': {  # Handler for Library
            'class': 'logging.NullHandler',
            'level': logging.DEBUG,
            'formatter': 'formatter'
        },
        'application_handler': {  # Handler for Application
            'class': 'logging.handlers.RotatingFileHandler',
            'level': logging.DEBUG,
            'formatter': 'formatter',
            'filename': 'logging.log',
            'mode': 'a',
            'maxBytes': 0,
            'backupCount': 0,
            'encoding': 'utf-8',
            'delay': False
        }
    },
    'formatters': {
        'formatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    }
})

logger = logging.getLogger(__name__)

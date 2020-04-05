import os

# Logging dict config
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default_f': {
            'format':'%(asctime)s - %(levelname)s - %(module)s:%(funcName)s - %(message)s'
        }
    },
    'handlers': {
        'default_h': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default_f',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'default_logger': {
            'level': 'INFO',
            'handlers': ['default_h']
        }
    }
}

# Output constants
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Course related constants
YEAR_CODE_2020 = "220"
YEAR_CODE_2021 = "221"
SEM_CODE_SPRING = "1"
SEM_CODE_FALL = "8"
SEM_CODE_SUMMER_1 = "6"
SEM_CODE_SUMMER_2 = "7"

# Shared data
QUERIED_SEMESTER = None
QUERIED_YEAR = None
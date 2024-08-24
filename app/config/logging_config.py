import logging
import logging.config
import sys
def setup_logging():
    logging_config = {
        # Dict config schema version for logging module (only supports
        # version 1 as of 6/2024)
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%d-%b-%y %H:%M:%S",
            },
        },
        "handlers": {
            "file": {
                "level": "DEBUG",
                "formatter": "standard",
                "class": "logging.FileHandler",
                "filename": "app/app.log",
                "mode": 'w',
                "encoding": "utf-8",
            },
            "console": {
                "level": "DEBUG",
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream" : sys.stdout
            },
        },
        "root": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
        },
    }
    logging.config.dictConfig(logging_config)

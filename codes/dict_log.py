#!/usr/bin/python

import logging
import logging.config


def configure_logging(logfile):
    fp = open(logfile, 'a+')
    log_config = {
        "version": 1,
	"formatters": {
	    "default": {
	        "format": '%(message)s'
	    }
	},
	"handlers": {
	    "console": {
	        "class": "logging.StreamHandler",
		"formatter": "default",
	    },
	    "file": {
	        "class": "logging.StreamHandler",
		"formatter": "default",
		"stream": fp
	    }
        },
	"loggers": {
	    "": {
		"handlers": ["console", "file"],
		"level": "DEBUG"
	    }
        }
    }

    logging.config.dictConfig(log_config)

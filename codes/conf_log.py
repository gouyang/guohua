#!/usr/bin/python

import logging
import logging.config
from StringIO import StringIO

def configure_logging(logfile):
    logconf = """
[loggers]
keys=root

[handlers]
keys=console, file

[formatters]
keys=verbose

[logger_root]
level=NOTSET
handlers=console, file

[handler_console]
class=StreamHandler
formatter=verbose
args=(sys.stdout,)

[handler_file]
class=FileHandler
formatter=verbose
args=('{0}', 'w')

[formatter_verbose]
format=%(message)s
""" 
    logging.config.fileConfig(StringIO(logconf.format(logfile)))

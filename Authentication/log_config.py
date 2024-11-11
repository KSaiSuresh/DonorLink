import logging
from logging.handlers import TimedRotatingFileHandler
from sys import stdout

def setup_logger(path="logs/fbase_logs.txt", level=logging.DEBUG):
                 format = logging.Formatter("%(asctime)s %(levelname)s %(funcName)s-%(lineno)s - %(message)s")
                 logger= logging.getLogger(__name__)
                 logger.setLevel(level)
                 consoleHandler = logging.StreamHandler(stdout) #set streamhandler to stdout
                 consoleHandler.setFormatter(format)
                 logger.addHandler(consoleHandler)
                 return logger

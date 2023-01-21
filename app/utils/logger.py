#-*- coding:utf-8 -*-
__author__      = "yongil80.cho@samsung.com"
__copyright__   = "Copyright 2022, Samsung Electronics"

import os
import sys
import time
import datetime

import logging
from logging import handlers
from colorlog import ColoredFormatter

basedir = os.path.abspath(os.path.dirname(__file__))

class SingletoneType(type):
    def __call__(cls, *args, **kwargs):
        __instance = None
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletoneType, cls).__call__(*args, **kwargs)
            return cls.__instance

class CustomLogger(object, metaclass=SingletoneType):
    def __init__(self):
        self._logger = None
        self._fileHandler = None
        self._streamHandler = None

        dirname = os.path.abspath(os.path.join(basedir, '../..', 'appdata', 'log'))
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        formatter_file = logging.Formatter('%(asctime)s %(levelname).1s %(message)s')
        formatter = ColoredFormatter(
            "%(log_color)s %(asctime)s %(levelname).1s %(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                'DEBUG':    'cyan,bold',
                'INFO':     '',
                'WARNING':  'yellow,bold',
                'ERROR':    'purple,bold',
                'CRITICAL': 'red,bold',
            },
            secondary_log_colors={},
            style='%'
        )
        self._fileHandler = handlers.TimedRotatingFileHandler(filename=os.path.join(dirname, 'app.log'), when='midnight', interval=1, encoding='utf-8')
        self._fileHandler.suffix = '%Y-%m-%d_%H-%M-%S'
        self._fileHandler.setFormatter(formatter_file)

        self._streamHandler = logging.StreamHandler(sys.stdout)
        self._streamHandler.setFormatter(formatter)

        self._logger = logging.getLogger("KPI-BOT")
        self._logger.setLevel(logging.DEBUG)
        logging.basicConfig(handlers=[self._streamHandler, self._fileHandler])

    @property
    def logger(self):
        return self._logger

    @property
    def fileHandler(self):
        return self._fileHandler

    @property
    def streamHandler(self):
        return self._streamHandler

def main():
    logger = CustomLogger.__call__().logger
    logger.info("mic test")

if __name__ == '__main__':
    sys.exit(main())

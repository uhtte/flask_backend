# -*- coding:utf-8 -*-
__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"

import os
import sys
from pathlib import Path



class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    PATH_MODEL = os.path.normpath(os.path.join(basedir, "../model"))
    PATH_OUTPUT = os.path.normpath(os.path.join(basedir, "../output"))
    PATH_UPLOAD = os.path.normpath(os.path.join(basedir, "../appdata/upload"))
    PATH_DATABASE = os.path.normpath(os.path.join(basedir, "../appdata/storage"))
    SSL_CERTFILE = os.path.normpath(
        os.path.join("/etc/letsencrypt/live/be.aipowered.kro.kr/fullchain.pem")
    )
    SSL_KEYFILE = os.path.normpath(
        os.path.join("/etc/letsencrypt/live/be.aipowered.kro.kr/privkey.pem")
    )
    SSL_PASSWORD = "aipowered"


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"


config_by_name = dict(dev=DevelopmentConfig(), prod=ProductionConfig())


def main():
    cfg = config_by_name["dev"]
    print(cfg.DEBUG)


if __name__ == "__main__":
    sys.exit(main())

# -*- coding:utf-8 -*-
import sys
from datetime import timedelta

from flask import Flask
from flask_cors import CORS

from app.config import config_by_name
from app.libs.controller import Controller

__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"

__appname__ = "MMC-SERVER"
__version__ = "0.0.0"


CONTROLLER = Controller()


def create_app(config_name):
    app = Flask(__name__)
    app.secret_key = "random key string"
    app.config.from_object(config_by_name[config_name])
    app.permanent_session_lifetime = timedelta(minutes=5)

    CORS(app, resources={r"/*": {"origins": "*"}})

    CONTROLLER.init(
        path_database=app.config["PATH_DATABASE"],
        path_upload=app.config["PATH_UPLOAD"],
        path_output=app.config["PATH_OUTPUT"],
        path_model=app.config["PATH_MODEL"],
    )

    return app

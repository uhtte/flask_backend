# -*- coding:utf-8 -*-
import os
import sys
from pathlib import Path

from werkzeug.utils import secure_filename

from app.libs.dbmgr import *
from app.libs.u2net_portrait import *
from app.utils.helper import *
from app.utils.logger import *

__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


logger = CustomLogger.__call__().logger


class Controller:
    def __init__(self):
        self._dbmgr = None
        self._path_model = None
        self._path_output = None
        self._path_upload = None

    def init(self, path_database, path_upload, path_output, path_model):
        self._dbmgr = DBManager(path_db=path_database)
        self._path_model = path_model
        self._path_output = path_output
        self._path_upload = path_upload
        Path(path_output).mkdir(exist_ok=True, parents=True)
        Path(path_upload).mkdir(exist_ok=True, parents=True)

    def start_tests(self):
        return

    def file_upload(self, file):
        logger.info(f"file_upload {file.filename}")

        filename = secure_filename(file.filename)
        os.makedirs(self._path_upload, exist_ok=True)
        file.save(os.path.join(self._path_upload, filename))

        u2net = U2Net_portrait(
            path_model=self._path_model, path_output=self._path_output
        )
        return u2net.run(os.path.normpath(os.path.join(self._path_upload, filename)))

    def file_download(self, filename):
        logger.info(f"file_download {filename}")
        return os.path.normpath(os.path.join(self._path_output, filename))

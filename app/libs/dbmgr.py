#-*- coding:utf-8 -*-
__author__      = "yongil80.cho@samsung.com"
__copyright__   = "Copyright 2022, Samsung Electronics"

import os
import sys
import threading
from tinydb import TinyDB, Query

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.helper import *
from utils.logger import *
logger = CustomLogger.__call__().logger

class DBManager():
    def __init__(self, path_db):
        self._dbpath = path_db
        self._lock = threading.Lock()

        if os.access(self._dbpath, os.F_OK) is False:
            logger.info(f'create db directory at {self._dbpath}')
            os.makedirs(self._dbpath)
        self._db = TinyDB(os.path.join(self._dbpath, 'local.json'))

    def __del__(self):
        if self._db != None:
            self._db.close()

    def _records_collection(self):
        return self._db.table('records')

    def flush_records(self):
        with self._lock:
            collection = self._records_collection()
            collection.truncate()
    
    def insert_record(self, record):
        with self._lock:
            collection = self._records_collection()
            new_id = collection.insert(record)
        return new_id

    def delete_records(self, query):
        with self._lock:
            collection = self._records_collection()
            collection.remove(query)

    def fetch_records(self, query=None):
        with self._lock:
            collection = self._records_collection()
            if query == None:
                items = collection.all()
            else:
                items = collection.search(query)
        return items
    
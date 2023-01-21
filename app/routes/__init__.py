#-*- coding:utf-8 -*-
__author__      = "yongil80.cho@samsung.com"
__copyright__   = "Copyright 2022, Samsung Electronics"

from . import api_image
from . import api_status

__all__ = ["blueprints"]

blueprints = [
    api_image.bp,
    api_status.bp
]
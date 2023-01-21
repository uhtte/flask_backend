# -*- coding:utf-8 -*-
from . import api_status
from . import api_image
__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"


__all__ = ["blueprints"]

blueprints = [
    api_image.bp,
    api_status.bp
]

# -*- coding:utf-8 -*-
from flask import Blueprint, jsonify, make_response, render_template, request, session

from app import CONTROLLER
from app.utils.helper import *
from app.utils.logger import *

__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"


logger = CustomLogger.__call__().logger

bp = Blueprint("api_status", __name__, url_prefix="/api/v1")

hdrs = {"Content-Type": "text/html"}


@bp.route("/get", methods=["GET"])
def get_api():
    try:
        data = {"message": "Done", "code": "OK"}
        return make_response(jsonify(data), 201, hdrs)
    except:
        data = {"message": "Ehhh", "code": "ERROR"}
        return make_response(jsonify(data), 200, hdrs)


@bp.route("/post", methods=["POST"])
def post_api():
    try:
        param = request.json

        data = {"message": "Done", "code": "OK"}
        return make_response(jsonify(data), 201, hdrs)
    except:
        data = {"message": "Ehhh", "code": "ERROR"}
        return make_response(jsonify(data), 200, hdrs)

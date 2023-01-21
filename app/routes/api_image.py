# -*- coding:utf-8 -*-
import base64
import io

from flask import (
    Blueprint,
    jsonify,
    make_response,
    render_template,
    request,
    send_file,
    session,
)
from PIL import Image

from app import CONTROLLER
from app.utils.helper import *
from app.utils.logger import *

__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"


logger = CustomLogger.__call__().logger

bp = Blueprint("api_image", __name__, url_prefix="/api/v1")

hdrs = {"Content-Type": "text/html"}


@bp.route("/file", methods=["POST"])
def api_upload():
    try:
        file = request.files["attached"]

        filename = CONTROLLER.file_upload(file)
        data = {"message": filename, "code": "OK"}
        return make_response(jsonify(data), 201, hdrs)
    except Exception as e:
        data = {"message": str(e), "code": "ERROR"}
        return make_response(jsonify(data), 200, hdrs)


@bp.route("/file/<string:filename>", methods=["GET"])
def api_download(filename):
    try:
        filepath = CONTROLLER.file_download(filename)
        img = Image.open(filepath, mode="r")
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")
        my_encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode("ascii")
        data = {"message": my_encoded_img, "code": "OK"}
        return make_response(jsonify(data), 200, hdrs)
        # return send_file(filepath, mimetype='image/gif')
    except Exception as e:
        data = {"message": str(e), "code": "ERROR"}
        return make_response(jsonify(data), 200, hdrs)

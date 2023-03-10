__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"

import sys

from flask import render_template
from pyfiglet import Figlet

from app import create_app
from app.routes import blueprints
from app.utils.helper import *
from app.utils.logger import *

# import ssl


logger = CustomLogger.__call__().logger

"""
 ENVIRONMENT VARIABLE
 - KPIBOT_MODE: 'dev' or 'prod'
"""
app = create_app(os.getenv("SERVER_MODE") or "prod")
# set routers
for bp in blueprints:
    app.register_blueprint(bp)

logging.getLogger("werkzeug").addHandler(CustomLogger.__call__().fileHandler)

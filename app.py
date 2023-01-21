__author__ = "yongil80.cho@samsung.com"
__copyright__ = "Copyright 2022, Samsung Electronics"

import sys
# import ssl

from pyfiglet import Figlet
from flask import render_template

from app import create_app
from app.routes import blueprints
from app.utils.helper import *
from app.utils.logger import *
logger = CustomLogger.__call__().logger

"""
 ENVIRONMENT VARIABLE
 - KPIBOT_MODE: 'dev' or 'prod'
"""
app = create_app(os.getenv('SERVER_MODE') or 'dev')
# set routers
for bp in blueprints:
    app.register_blueprint(bp)

logging.getLogger('werkzeug').addHandler(CustomLogger.__call__().fileHandler)

"""
"""


def main(argv):
    print(Figlet(font='slant').renderText('MMC SERVER '))

    logger.info('service is running!')
    try:
        # ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        # ssl_context.load_cert_chain(certfile=app.config['SSL_CERTFILE'], keyfile=app.config['SSL_KEYFILE'], password=app.config['SSL_PASSWORD'])
        # app.run(use_reloader=False, threaded=True, host='0.0.0.0', port=7777, ssl_context=ssl_context)
        app.run(use_reloader=False, threaded=True)
        # app.run(threaded=True, host=socket.gethostbyname(socket.gethostname()))
    except:
        logger.critical(get_callstack())
    logger.info('service is finished!')


if __name__ == '__main__':
    sys.exit(main(sys.argv))

import os
from flask import (
    Flask,
    current_app,
    request,
    g,
    Blueprint,
    render_template,
    make_response,
)
from wheelie import car


drive_bp = Blueprint('drive', __name__)


@drive_bp.route("/drive", methods=['POST'])
def drive():
    if request.method == "POST":
        data = request.form

        speed = float(data['speed'])
        if -1 > speed or speed > 1:
            return make_response('bad speed', 200)

        turn = float(data['turn'])
        if -1 > turn or turn > 1:
            return make_response('bad turn', 200)

        car.speed(abs(speed))
        car.turn_speed(abs(turn))
        if turn < 0:
            car.turn_left()
        if turn > 0:
            car.turn_right()
        if turn == 0:
            car.straight()
        if speed > 0:
            car.forward()
        if speed < 0:
            car.reverse()
        if speed == 0:
            car.stop()

        return make_response('', 200)


class Config:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJET_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = 'simple'
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_HEADERS_PREFIX = 'Token'
    CORS_ORIGIN_WHITELIST = []
    JWT_HEADER_TYPE = 'Token'
    CSRF_ENABLED = True
    DEBUG = False


def create_app():
    app = Flask(__name__.split('.')[0], static_url_path='/static')
    app.url_map.strict_slashes = False
    app.config.from_object(Config)
    app.register_blueprint(drive_bp)

    return app

from flask import Blueprint

frontend = Blueprint('frontend', __name__) # No url_prefix here, so it's at the root

@frontend.route('/')
def index():
    return "Welcome to HeyApp!"

@frontend.route('/healthz', methods=['GET'])
def healthz():
    return "OK"


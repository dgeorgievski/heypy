"""
    Factory function to create a Flask application instance 
"""
import os
from flask import Flask
from config import config # Import the config dictionary
from heyapp.views.frontend import frontend

def create_app(config_name=None):
    '''
    Create a Flask application instance.
    '''
    app = Flask(__name__)

    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'default') # Get from env or use 'default'

    app.config.from_object(config[config_name])
    config[config_name].init_app(app) # Call the static init_app method

    # Register the blueprints with the main app
    app.register_blueprint(frontend)

    return app

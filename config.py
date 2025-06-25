# config.py
import os

# Get the base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_dev_secret_key_if_env_not_set'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMIN_EMAIL = 'admin@example.com'

    @staticmethod
    def init_app(app):
        # This method can be used to perform any app-specific initialization
        # that depends on the config, e.g., logging setup.
        pass

class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    """Testing environment configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///:memory:' # In-memory database for faster tests

class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False # Should always be False in production
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://user:password@host/prod_db' # Example for PostgreSQL

    # More specific production settings
    MAIL_USE_TLS = False # Might use SSL on a different port or a service like SendGrid
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    # For production, it's highly recommended to use environment variables for sensitive info
    # and not provide default values for them.
    SECRET_KEY = os.environ.get('SECRET_KEY') # No default, force env var in production

# A dictionary to easily map configuration names to their classes
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig # Set a default config
}

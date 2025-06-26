import sys
import os
import pytest

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from heyapp import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "testing": True,
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

import os
import tempfile
import pytest

from hays_1 import create_app


@pytest.yield_fixture(scope="session")
def app():
    """
    Setup flask test app

    : return : flask app 
    """
    params = {"DEBUG": False, "TESTING": True, "SERVER_NAME": "localhost.localdomain"}

    app = create_app(settings_override=params)

    app_ctx = app.app_context()
    app_ctx.push()

    yield app


@pytest.yield_fixture(scope="function")
def client(app):
    """
    Setsup a client for the app

    :param app: fixture
    :return: flask app client
    """
    yield app.test_client()


import os

from flask import Flask
from werkzeug.security import check_password_hash, generate_password_hash

from celery import Celery


from flask_sqlalchemy import SQLAlchemy
from hays_1.config import Config
from hays_1 import celeryconfig

db = SQLAlchemy()


def create_celery_app(app=None):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return: Celery app
    """
    app = app or create_app()

    celery = Celery(app.import_name, broker=app.config["CELERY_BROKER_URL"])
    celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(settings_override=None):
    """ Creates python flask app using the app factorry pattern.

    : param settings_override: Override settings
    : return : Flask app      
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    if settings_override:
        app.config.update(settings_override)

    db.init_app(app)

    from hays_1.contacts.routes import contact
    from hays_1.main.routes import main

    app.register_blueprint(contact)
    app.register_blueprint(main)

    return app

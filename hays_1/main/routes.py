from flask import (
    Flask,
    render_template,
    redirect,
    render_template,
    url_for,
    flash,
    request,
    Blueprint,
)
from flask_login import current_user

from faker import Faker
from hays_1.models import Contact
from hays_1 import db


fake_data = Faker()


main = Blueprint("main", __name__)

"""
currently empty

"""

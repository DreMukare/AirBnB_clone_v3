#!/usr/bin/python3

"""creates api
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import Blueprint

app = Flask(__name__)
app.register_blueprint(app_views)


if __name__ = "__main__":


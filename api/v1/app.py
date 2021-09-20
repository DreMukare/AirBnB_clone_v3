#!/usr/bin/python3

"""creates api
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)
api_host = environ['HBNB_API_HOST']
api_port = environ['HBNB_API_PORT']


@app.teardown_appcontext
def teardown(exc):
    """removes the current sqlalchemy session"""
    storage.close()


if __name__ = "__main__":
    if api_host is None and api_port is None:
        app.run(host='0.0.0.0', port='5000', threaded=True)
    elif api_host is not None and api_port is None:
        app.run(host=api_host, port='5000', threaded=True)
    elif api_host is None and api_port is not None:
        app.run(host='0.0.0.0', port=api_port, threaded=True)
    else:
        app.run(host=api_host, port=api_port, threaded=True)

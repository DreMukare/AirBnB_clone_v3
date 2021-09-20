#!/usr/bin/python3

"""creates api
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
api_host = environ['HBNB_API_HOST']
api_port = environ['HBNB_API_PORT']


@app.teardown_appcontext
def teardown(exc):
    """removes the current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', '5000')))

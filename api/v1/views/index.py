#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify


@app.views.route("/status", strict_slashes=False)
def status():
    """returns JSON status"""
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    pass

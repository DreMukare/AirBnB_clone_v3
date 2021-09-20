#!/usr/bin/python3
'''handles starting of api'''

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app.views.route("/status", strict_slashes=False)
def status():
    """returns JSON status"""
    return jsonify({'status': 'OK'})


@app.views.route('/api/v1/stats', strict_slashes=False)
def stats():
    """retrieves number of each obj by type"""
    classes = {
        'amenities': 'Amenity',
        'cities': 'City',
        'places': 'Place',
        'reviews': 'Review',
        'states': 'State',
        'users': 'User'
    }
    output = {}
    for key, value in classes.items():
        output[key] = storage.count(value)
    return jsonify(output)


if __name__ == '__main__':
    pass

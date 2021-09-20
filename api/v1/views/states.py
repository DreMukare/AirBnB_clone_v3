#!/usr/bin/python3
'''view for State objects'''

from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, make_response
from models.state import State
from models import storage


@app.views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    '''returns all states'''
    output = []
    for state in storage.all('State').values():
        output.append(state.to_dict())
    return jsonify(output)


@app.views.route('states/<string:state_id>',
                 methods=['GET'], strict_slashes=False)
def one_state(state_id):
    '''returns state based on id'''
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app.views.route('states/<string:state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    '''deletes state obj'''
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_state():
    """create a new state"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state = State(**request.get_json())
    state.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state(state_id):
    """update a state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(state, attr, val)
    state.save()
    return jsonify(state.to_dict())

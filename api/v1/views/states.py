#!/usr/bin/python3
"""Routes for States API"""
from models import storage 
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Shows all states.
           Returns:
               A list of JSON disctionaries of all states.
    """
    states = list(storage.all('State').values())
    states_list = []
    for state in states:
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Shows a specific state based on id.
           Parameters:
               state_id [str]: the id of the state to display
           Returns:
               A JSON dictionary of the state in a 200 response
               A 404 response if the id does not match
    """
    state = storage.get('State', state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a specific state.
            Parameters:
                state_id [str]: the id of the state
            Returns:
                An empty JSON dictionary in a 200 response.
                a 404 response if the id does not match.
    """
    state = storage.get('State', state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state():

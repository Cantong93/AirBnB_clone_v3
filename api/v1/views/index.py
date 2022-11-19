#!/usr/bin/python3
storage_get_count
"""create a route /status on the object app_views that
returns a JSON: 'status': 'OK'"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """status"""

"""Routing for views"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes-False)
def show_status():
    """Shows the status of the API
         Returns:
             A JSON string of the status
    """
master
    return jsonify({'status': 'OK'})

#!/usr/bin/python3
"""
	State view for api/v1
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, make_response, abort
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
	""" Function to list all states Obj """
	all_states = storage.all(State).values()
	state_list = []
	for states in all_states:
		state_list.append(states.to_dict())
	return jsonify(state_list)

@app_views.route('/states/<state_id>', methods=['GET'],
				  strict_slashes=False)
def state_by_id(state_id):
	""" Get a particular state by Id """
	try:
		stateI = storage.get(State, id=state_id)
		return jsonify(stateI.to_dict())
	except Exception:
		abort(404)
		#return make_response({"error": "Not found"}, 404)

@app_views.route('/states/<state_id>', methods=['DELETE'],
				  strict_slashes=False)
def delete_state_id(state_id):
	""" Get a particular state by Id """
	try:
		stateI = storage.get(State, id=state_id)
		storage.delete(stateI)
		storage.save()
		return make_response(jsonify({}), 200)
	except Exception:
		abort(404)
		#return make_response({"error": "Not found"}, 404)

@app_views.route('/states', methods=['POST'],
				  strict_slashes=False)
def post_state():
	""" Get a particular state by Id """
	data = request.get_json()
	if data is None:
		abort(400, description="Not a JSON")
	if "name" not in data:
		abort(400, description="Missing name")
	new_state = State(**data)
	new_state.save()
	return make_response(jsonify(new_state.to_dict()), 201)

@app_views.route('/states/<state_id>', methods=['PUT'],
				  strict_slashes=False)
def edit_state(state_id):
	""" Get a particular state by Id """
	data = request.get_json()
	if data is None:
		abort(400, description='Not a JSON')
	state = storage.get(State, id=state_id)
	if state is None:
		abort(404)
	ignore_list = ['id', 'created_at', 'updated_at']
	for k, v in data.items():
		if k not in ignore_list:
			setattr(state, k, v)
	state.save()
	return make_response(jsonify(state.to_dict(), 200))
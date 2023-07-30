#!/usr/bin/python3
""" Index page for v1 API """
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


stats = {
	'status': 'OK'
}

site_stats = {
  "amenities": storage.count(Amenity), 
  "cities": storage.count(Amenity), 
  "places": storage.count(Place), 
  "reviews": storage.count(Review), 
  "states": storage.count(State), 
  "users": storage.count(User)
}

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
	""" Index api for AirBnB v1"""
	return jsonify(stats)

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stat():
	""" Get status about all classes """
	return jsonify(site_stats)

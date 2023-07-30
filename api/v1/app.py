#!/usr/bin/python3
""" AirBnB API """
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv

HOST = getenv('HBNB_API_HOST')
PORT = getenv('HBNB_API_PORT')

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(obj):
	""" Closes storage after usage """
	storage.close()

@app.errorhandler(404)
def err404(err):
	""" Error message to return """
	return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
	if HOST and PORT:
		app.run(host=HOST, port=PORT, debug=True, threaded=True)
	else:
		app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
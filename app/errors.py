from flask import jsonify
from app import app


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"message": "404 Not Found"}), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"message": "405 Method Not Allowed"}), 405


@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"message": error.description}), 400

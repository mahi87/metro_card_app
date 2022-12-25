from app import app
from flask import jsonify


@app.route("/v1/metro_card", methods=["POST"])
def create_metro_card():
    return jsonify({"message": "creating metro card"})


@app.route("/v1/metro_card", methods=["GET"])
def get_all_metro_cards():
    return jsonify({"message": "get all metro card"})


@app.route("/v1/metro_card/<id>", methods=["GET"])
def get_metro_card(id):
    return jsonify({"message": "getting card details"})


@app.route("/v1/metro_card/<id>", methods=["PUT"])
def update_metro_card(id):
    return jsonify({"message": "updating card details"})


@app.route("/v1/metro_card/<id>", methods=["DELETE"])
def delete_metro_card(id):
    return jsonify({"message": "deleting card details"})

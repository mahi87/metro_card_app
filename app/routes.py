from app import app, db
from flask import jsonify, request
from .models import MetroCard


@app.route("/v1/metro_card", methods=["POST"])
def create_metro_card():
    content = request.json
    if "name" not in content or "pin" not in content:
        return jsonify({"message": "missing name/pin args"}), 400
    metro_card = MetroCard(name=content["name"])
    metro_card.set_pin(content["pin"])
    db.session.add(metro_card)
    db.session.commit()
    return jsonify({"id": metro_card.id}), 201


@app.route("/v1/metro_card", methods=["GET"])
def get_all_metro_cards():
    metro_card = MetroCard.query.order_by("id").all()
    res = []
    for card in metro_card:
        res.append({"id": card.id, "name": card.name, "balance": card.balance})
    return jsonify(res)


@app.route("/v1/metro_card/<id>", methods=["GET"])
def get_metro_card(id):
    metro_card = MetroCard.query.get_or_404(id)
    res = {"id": metro_card.id, "name": metro_card.name, "balance": metro_card.balance}
    return jsonify(res)


@app.route("/v1/metro_card/<id>", methods=["PUT"])
def update_metro_card(id):
    return jsonify({"message": "updating card details"})


@app.route("/v1/metro_card/<id>", methods=["DELETE"])
def delete_metro_card(id):
    return jsonify({"message": "deleting card details"})

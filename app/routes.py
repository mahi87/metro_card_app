from app import app, db
from flask import jsonify, request, abort
from .models import MetroCard, Station


@app.route("/v1/metro_card", methods=["POST"])
def create_metro_card():
    content = request.json
    if "name" not in content or "pin" not in content:
        abort(400, description="missing name/pin args")
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
    content = request.json
    if "name" not in content or "balance" not in content:
        abort(400, description="Missing required args in request")
    metro_card = MetroCard.query.get_or_404(id)
    metro_card.balance = content["balance"]
    metro_card.name = content["name"]
    db.session.add(metro_card)
    db.session.commit()
    res = {"name": metro_card.name, "id": metro_card.id, "balance": metro_card.balance}
    return jsonify(res)


@app.route("/v1/metro_card/<id>", methods=["DELETE"])
def delete_metro_card(id):
    metro_card = MetroCard.query.get_or_404(id)
    db.session.delete(metro_card)
    db.session.commit()
    return jsonify({"message": f"Metro card with id {id} has been deleted"})


@app.route("/v1/station", methods=["POST"])
def create_station():
    content = request.json
    if "name" not in content:
        abort(400, description="name missing in request")
    s = Station(name=content["name"])
    db.session.add(s)
    db.session.commit()
    return jsonify({"id": s.id}), 201

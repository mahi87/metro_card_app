from app import app


@app.route("/v1/metro_card", methods=["POST"])
def create_metro_card():
    return "creating metro card"


@app.route("/v1/metro_card", methods=["GET"])
def get_all_metro_cards():
    return "get all metro card"


@app.route("/v1/metro_card/<id>", methods=["GET"])
def get_metro_card(id):
    return "getting card details"


@app.route("/v1/metro_card/<id>", methods=["PUT"])
def update_metro_card(id):
    return "updating metro card"


@app.route("/v1/metro_card/<id>", methods=["DELETE"])
def delete_metro_card(id):
    return "deleting metro card"

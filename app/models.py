from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class MetroCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Integer, default=0, nullable=False)
    pin_hash = db.Column(db.String(128), nullable=False)
    dob = db.Column(db.DateTime)

    def set_pin(self, pin):
        self.pin_hash = generate_password_hash(pin)

    def check_pin(self, pin):
        return check_password_hash(self.pin_hash, pin)

    def deduct_balance(self, amount):
        self.balance = self.balance - amount

    def passenger_type(self):
        if self.dob is None:
            return "UNKNOWN"
        age_delta = datetime.now() - self.dob
        age = (age_delta.days) // 365
        if 0 <= age <= 18:
            return "KID"
        elif 18 < age <= 50:
            return "ADULT"
        else:
            return "SENIOR_CITIZEN"


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    total_collection = db.Column(db.Integer, default=0)
    total_discount = db.Column(db.Integer, default=0)
    passenger_adult = db.Column(db.Integer, default=0)
    passenger_kid = db.Column(db.Integer, default=0)
    passenger_senior_citizen = db.Column(db.Integer, default=0)


class Journey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metro_card_id = db.Column(db.Integer, db.ForeignKey("metro_card.id"))
    from_station_id = db.Column(db.Integer, db.ForeignKey("station.id"))
    to_station_id = db.Column(db.Integer, db.ForeignKey("station.id"))

    def charges(self):
        charges = {"ADULT": 200, "KID": 50, "SENIOR_CITIZEN": 100, "UNKNOWN": 500}
        metro_card = MetroCard.query.get(self.metro_card_id)
        return charges[metro_card.passenger_type()]

from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash


class MetroCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Integer, default=0, nullable=False)
    pin_hash = db.Column(db.String(128), nullable=False)

    def set_pin(self, pin):
        self.pin_hash = generate_password_hash(pin)

    def check_pin(self, pin):
        return check_password_hash(self.pin_hash, pin)


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    total_collection = db.Column(db.Integer, default=0)
    total_discount = db.Column(db.Integer, default=0)
    passenger_adult = db.Column(db.Integer, default=0)
    passenger_kid = db.Column(db.Integer, default=0)
    passenger_senior_citizen = db.Column(db.Integer, default=0)

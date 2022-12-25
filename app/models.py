from app import app, db


class MetroCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    pin_hash = db.Column(db.String(128), nullable=False)

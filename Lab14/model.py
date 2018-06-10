from app import db


class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(50))
    price = db.Column(db.Integer)
    country_from = db.Column(db.String(50))
from app import db


class MusicInstrument(db.Model):
    __tablename__ = "musical_instrument"
    musical_instrument_id = db.Column('id', db.Integer, primary_key=True)
    musical_instrument_price = db.Column('price_of_instruments', db.String(20))
    musical_instrument_price = db.Column('price', db.Integer, primary_key=True)
    musical_instrument_country_from = db.Column('country_from', db.String(20))

def __str__(self):
    return str("instrument id: ", str(self.musical_instrument_id) + "\nInstrument price: ", str(self.musical_instrument_price) +
               + "\nPrice: ", str(self.musical_instrument_price) + "\nCountry from: ", str(self.musical_instrument_price_country_from))
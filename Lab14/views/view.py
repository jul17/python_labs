from email.mime import application

from flask import request, app

from music_instrument import MusicInstrument


@application.route('/')
def index():
    first_num = MusicInstrument.querty.first()
    return '<h1> Here you can find music instrument list! </h1>'

@application.route('/')
def view():
    instrument = MusicInstrument.querty.first()
    if instrument is not None:
        return str('Firat member name \n' + instrument.__str__())
    else:
        return "Music Instrument with this id does not exist"

@application.route('/music/<id>')
def get(id):
    instrument = MusicInstrument.querty.get(id)
    if instrument is not None:
        return instrument.__str__()
    else:
        return "Music Instrument with this id does not exist"

@application.route('/music', methods = ['POST'])
def add_in():
    instrument_id = request.json['id']
    price_of_instrument = request.json['price_of_instrument']
    price = request.json['price']
    country_from = request.json['country_from']

    new_instrument = MusicInstrument()
    new_instrument.musical_instrument_id = instrument_id
    new_instrument.musical_instrument_price = price_of_instrument
    new_instrument.musical_instrument_price = price
    new_instrument.musical_instrument_price_country_from = country_from

    app.db.session.add(new_instrument)
    app.db.session.commit()

    return str(new_instrument.__str__())

@application.route('/music/<id>', methods = ['PUT'])
def update(id):
    price_of_instrument = request.json['price_of_instrument']
    price = request.json['price']
    country_from = request.json['country_from']

    new_instrument = MusicInstrument.querty.get(id)
    new_instrument.devise_id = id
    new_instrument.devise_model = price_of_instrument
    new_instrument.device_producer = price
    new_instrument.devise_power = country_from

    app.db.session.commit()
    return new_instrument.__str__()

@application.route('/music/<id>', methods = ['DELETE'])
def delete(id):
    instrument = MusicInstrument.querty.get(id)
    app.db.session.delete(instrument)
    app.db.session.commit()

    return str("Deleting successful")
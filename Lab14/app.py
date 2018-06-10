from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ma = Marshmallow(app)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

import sys

sys.path.insert(0, 'views')


if __name__ == '__main__':
    app.run()

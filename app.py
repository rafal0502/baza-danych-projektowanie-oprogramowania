from flask import Flask, jsonify
from models.KlientModel import KlientModel
from flask_restful import Api, Resource
from models.DanieModel import DanieModel
from models.PracownikModel import PracownikModel
from resources.klient import Klient


app = Flask(__name__)
api = Api(app)
app.secret_key = 'projekt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# @app.before_first_request
# def create_tables():
#     db.create_all()


api.add_resource(Klient, '/klient/<string:id_klienta>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5001, debug=True)

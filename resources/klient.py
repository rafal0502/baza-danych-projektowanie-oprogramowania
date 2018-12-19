import sqlite3
from models.KlientModel import KlientModel
from flask_restful import Resource


class Klient(Resource):
    def get(self, id_klienta):
        klient = KlientModel.find_klient_by_id(id_klienta)
        if klient:
            return klient.json()
        return {'message': 'Store not found'}, 404







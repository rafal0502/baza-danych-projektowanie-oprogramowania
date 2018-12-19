import sqlite3
from db import db

class DanieModel(db.Model):
    __tablename__ = 'Danie'
    __table_args__ = {'extend_existing': True}

    id_dania = db.Column(db.String(), primary_key=True)
    id_restauracji = db.Column(db.String())
    nazwa = db.Column(db.String())
    cena = db.Column(db.Float(precision=2))
    opis = db.Column(db.String())


    def __init__(self, id_dania, nazwa, cena='', opis='', id_restauracji=''):
        self.id_dania = id_dania
        self.id_restauracji = id_restauracji
        self.nazwa = nazwa
        self.cena = cena
        self.opis = opis

    def insert(self):
        db.session.add(self)
        db.session.commit()
        db.session.close()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        db.session.close()

    @classmethod
    def find_danie_by_id(cls, id_dania):
        return cls.query.filter_by(id_dania=id_dania).first()


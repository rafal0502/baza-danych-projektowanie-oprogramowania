import sqlite3
from db import db


class KlientModel(db.Model):
    __tablename__ = 'Klient'
    __table_args__ = {'extend_existing': True}

    id_klienta = db.Column(db.String(20), primary_key=True)
    haslo = db.Column(db.String(20))
    imie = db.Column(db.String(20))
    nazwisko = db.Column(db.String(20))
    adres = db.Column(db.String())
    email = db.Column(db.Integer())
    telefon = db.Column(db.Integer())
    punkty = db.Column(db.Integer())

    def __init__(self, id_klienta, imie, nazwisko, telefon, haslo, email, adres, punkty):
        self.id_klienta = id_klienta
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.haslo = haslo
        self.email = email
        self.adres = adres
        self.punkty = punkty

    def insert(self):
        db.session.add(self)
        db.session.commit()
        db.session.close()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        db.session.close()

    def json(self):
        return {"id_klienta": self.id_klienta, "imie": self.imie, "nazwisko": self.nazwisko, "adres": self.adres, "email": self.email,
                "telefon": self.telefon, "punkty": self.punkty}

    @classmethod
    def find_klient_by_id(cls, id_klienta):
        return cls.query.filter_by(id_klienta=id_klienta).first()






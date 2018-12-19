import sqlite3
from db import db

class PracownikModel(db.Model):
    __tablename__ = 'Pracownik'
    __table_args__ = {'extend_existing': True}

    id_pracownika = db.Column(db.String(20), primary_key=True)
    id_restauracji = db.Column(db.String(20))
    imie = db.Column(db.String(20))
    nazwisko = db.Column(db.String())
    telefon = db.Column(db.Integer())
    stanowisko = db.Column(db.String())
    haslo = db.Column(db.String(20))


    def __init__(self, id_pracownika, id_restauracji, imie, nazwisko, telefon, stanowisko, haslo):
        self.id_pracownika = id_pracownika
        self.id_restauracji = id_restauracji
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.stanowisko = stanowisko
        self.haslo = haslo

    def insert(self):
        db.session.add(self)
        db.session.commit()
        db.session.close()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        db.session.close()

    def json(self):
        return {'id_pracownika': self.id_pracownika, 'id_restauracji': self.id_restauracji, 'imie': self.imie,
                'nazwisko': self.nazwisko, 'telefon': self.telefon, 'stanowisko': self.stanowisko}

    @classmethod
    def find_pracownik_by_id(cls, id_pracownika):
        return cls.query.filter_by(id_pracownika=id_pracownika).first()
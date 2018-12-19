import sqlite3
import os.path


my_path = os.path.abspath(os.path.dirname("db"))
database_path = os.path.join(my_path, "database.db")


class Klient():
    def __init__(self, id_klienta,  imie, nazwisko, telefon, haslo,  email,adres, punkty):
        self.id_klienta = id_klienta
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.haslo = haslo
        self.email = email
        self.adres = adres
        self.punkty = punkty

    def insert(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        query = "INSERT INTO Klient VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (self.id_klienta, self.imie, self.nazwisko,self.telefon, self.haslo, self.email, self.adres, self.punkty))
        conn.commit()
        conn.close()


class Pracownik:
    def __init__(self, id_pracownika, id_restauracji, imie, nazwisko, telefon, stanowisko, haslo):
        self.id_pracownika = id_pracownika
        self.id_restauracji = id_restauracji
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.stanowisko = stanowisko
        self.haslo = haslo

    def json(self):
        return {'id_pracownika': self.id_pracownika, 'id_restauracji': self.id_restauracji, 'imie': self.imie,
                'nazwisko': self.nazwisko, 'telefon': self.telefon, 'stanowisko': self.stanowisko}


    def insert(self):
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()
            query = "INSERT INTO Pracownik VALUES (?,?,?,?,?,?,?)"
            cursor.execute(query, (self.id_pracownika, self.id_restauracji, self.imie, self.nazwisko,  self.telefon, self.stanowisko, self.haslo))
            conn.commit()
            conn.close()



class Restauracja:
    def __init__(self, id_restauracji, nazwa, adres):
        self.id_restauracji = id_restauracji
        self.nazwa = nazwa
        self.adres = adres

    def json(self):
        return {'id_restauracji': self.id_restauracji, 'nazwa': self.nazwa, 'adres': self.nazwa}

    def insert(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        query = "INSERT INTO Restauracja VALUES (?,?,?)"
        cursor.execute(query, (self.id_restauracji, self.nazwa, self.adres))
        conn.commit()
        conn.close()


class Zamowienie:
    def __init__(self, id_zamowienia, id_klienta, id_restauracji, kwota, status, oplacone, data_dodania, czas_dostawy, czas_realizacji, data_zlozenia, ocena, miasto, adres):
        self.id_zamowienia = id_zamowienia
        self.id_klienta = id_klienta
        self.id_restauracji = id_restauracji
        self.kwota = kwota
        self.status = status
        self.oplacone = oplacone
        self.data_dodania = data_dodania
        self.czas_dostawy = czas_dostawy
        self.czas_realizacji = czas_realizacji
        self.data_zlozenia = data_zlozenia
        self.ocena = ocena
        self.miasto = miasto
        self.adres = adres

    def insert(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        query = "INSERT INTO Zamowienie VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(query, (self.id_zamowienia, self.id_klienta, self.id_restauracji, self.kwota,  self.status, self.oplacone, self.data_dodania,
                               self.czas_dostawy, self.czas_realizacji, self.data_zlozenia, self.ocena, self.miasto, self.adres))
        conn.commit()
        conn.close()


class Danie:
    def __init__(self, id_dania, nazwa, cena='', opis='', id_restauracji=''):
        self.id_dania = id_dania
        self.id_restauracji = id_restauracji
        self.nazwa = nazwa
        self.cena = cena
        self.opis = opis

    def insert(self):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        query = "INSERT INTO Danie VALUES (?,?,?,?,?)"
        cursor.execute(query, (self.id_dania, self.id_restauracji, self.nazwa, self.cena, self.opis))
        conn.commit()
        conn.close()




Klient('heheszek', 'Jan', 'Kowalski', '333444555', 'wdjfh', 'jan@jan.pl', 'Konwaliowa 3', 3).insert()
Klient('silacz', 'Arnold', 'Czarny', '333444555', 'wdjfh', 'get@tothe.chopper', 'Terminowa 2', 3).insert()
Klient('SyLweK', 'Sykwester', 'Stalowy', '333444555', 'wdjfh', 'ramob@bumbum.rpg', 'Wybuchowa 4', 0).insert()
Pracownik('janPan', 1, 'Jan', 'Nowak', '123456789', 'pracownik kuchni', 'soicrupogi').insert()
Pracownik('AAmen',  2, 'Andrzej', 'Adrianowski', '777888999', 'dostawca', '39084utco').insert()
Pracownik('KNow', 1, 'Kasia', 'Nowak', '333444555', 'menadzer restauracji', 'kKdPS').insert()
Pracownik('rahim', 2, 'Rahim', 'bin Amdel', '333444555', 'menadzer restauracji', 'wdjfh').insert()
Pracownik('gracia12', 3, 'Grażyna', 'Nowak', '333444555', 'menadzer restauracji', 'pjdp').insert()
Pracownik('lubDum', 4, 'Robert','Kowalak', '333444555', 'menadzer restauracji', 'alkdjflk').insert()
Restauracja(1, 'Cebuliowo', 'Bitwy 17').insert()
Restauracja(2, 'Pizza House', 'Okopowa 2').insert()
Restauracja(3, 'Students Dream', 'Granadierow 5').insert()
Restauracja(4, 'Zew Mięsa', 'Mięsna 35').insert()
Restauracja(5, 'Piwowo', 'Browarna 46').insert()
Danie(id_dania=1, nazwa='Kawa').insert()
Danie(id_dania=2, nazwa='Ciastko').insert()
Danie(3, 'Bulka').insert()


zamowienia = [
    Zamowienie(1, 1, 1, 26.88, 'oczekujace', False, '', '', '', '2018-09-10', 2, 'Warszawa', "Grunwaldzka 13"),
    Zamowienie(2, 2, 1, 59.88, 'dostarczone', True, '', '', '', '2018-09-10', 4, 'Gdynia', "Wolności 15"),
    Zamowienie(3, 1, 1, 43.80, 'anulowane', False, '', '', '', '2018-09-10', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(5, 1, 1, 43.80, 'dostarczone', True, '2018-12-16', 72, 45, '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(6, 1, 1, 43.80, 'dostarczone', True, '2018-12-16', 12, 25, '', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(7, 1, 1, 43.80, 'anulowane', False, '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(8, 1, 1, 43.80, 'anulowane', False, '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(9, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(10, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(11, 1, 1, 43.80, 'dostarczone', True, '2018-12-16', 32, 44, '', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(12, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(13, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(14, 1, 1, 43.80, 'dostarczone', True, '', 18, 67, '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(15, 1, 1, 43.80, 'dostarczone', True, '', 32, 85, '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(16, 1, 1, 26.88, 'dostarczone', True, '', 22, 15, '2018-09-10', 2, 'Warszawa', "Grunwaldzka 13"),
    Zamowienie(17, 2, 1, 59.88, 'dostarczone', True, '', 10, 28, '2018-06-11', 4, 'Gdynia', "Wolności 15"),
    Zamowienie(18, 1, 1, 43.88, 'anulowane', '', '', 10, 28, '2018-12-16', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(19, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(20, 1, 1, 43.80, 'dostarczone', True, '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(21, 1, 1, 43.80, 'dostarczone', True, '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(22, 1, 1, 43.80, 'anulowane', True, '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(23, 1, 1, 43.80, 'anulowane', True, '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(24, 1, 1, 43.80, 'anulowane', True, '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(25, 1, 1, 43.80, 'anulowane', True, '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(26, 1, 1, 43.80, 'dostarczone', True, '', '', '', '2018-12-16', 12, 'Radom', "Alternatywy 4"),
    Zamowienie(27, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(28, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(29, 1, 1, 43.80, 'dostarczone', True, '', 58, 13, '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(30, 1, 1, 43.80, 'anulowane', True, '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(31, 1, 1, 26.88, 'oczekujace', '', '2018-09-10', '', '', '2018-12-16', 2, 'Warszawa', "Grunwaldzka 13"),
    Zamowienie(32, 2, 1, 59.88, 'dostarczone', True, '', 72, 45, '2018-09-10', 4, 'Gdynia', "Wolności 15"),
    Zamowienie(33, 2, 1, 43.80, 'anulowane', '', '', '', '', '2018-09-10', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(34, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-09-10', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(35, 1, 1, 43.80, 'dostarczone', True, '', 19, 56, '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(36, 1, 1, 43.80, 'dostarczone', True, '', 14, 37, '2018-12-26', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(37, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(38, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(39, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(40, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(41, 1, 1, 43.80, 'dostarczone', True, '', '', '', '2018-12-16', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(42, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(43, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(44, 1, 1, 43.80, 'dostarczone', True, '', 12, 17, '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(45, 1, 1, 43.80, 'dostarczone', True, '', 52, 17, '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(46, 1, 1, 26.88, 'dostarczone', True, '', 18, 38, '2018-09-10', 2, 'Warszawa', "Grunwaldzka 13"),
    Zamowienie(47, 2, 1, 59.88, 'dostarczone', True, '', 42, 18, '2018-06-11', 4, 'Gdynia', "Wolności 15"),
    Zamowienie(48, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(49, 1, 1, 43.88, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(50, 1, 1, 43.80, 'dostarczone', True, '', 72, 45, '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(51, 1, 1, 43.80, 'dostarczone', True, '', 42, 18, '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(52, 1, 1, 43.80, 'anulowane', True, '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(53, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(54, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(55, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(56, 1, 1, 43.80, 'dostarczone', True, '', 25, 75, '2018-12-16', 8, 'Radom', "Alternatywy 4"),
    Zamowienie(57, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
    Zamowienie(58, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(59, 1, 1, 43.80, 'dostarczone', True, '', 24, 18, '2018-12-16', 8, 'Warszawa', "Alternatywy 4"),
    Zamowienie(60, 1, 1, 43.80, 'anulowane', '', '', '', '', '2018-12-16', 8, 'Gdynia', "Alternatywy 4"),
]

for x in zamowienia:
    x.insert()






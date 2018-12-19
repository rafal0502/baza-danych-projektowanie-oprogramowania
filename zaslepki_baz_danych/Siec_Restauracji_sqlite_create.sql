CREATE TABLE Klient (
	id_klienta string PRIMARY KEY,
	imie string,
	nazwisko string,
	telefon string,
	haslo string,
	email string,
	adres string,
	punkty integer
);

CREATE TABLE Pracownik (
	id_pracownika string PRIMARY KEY,
	id_restauracji integer,
	imie string,
	nazwisko string,
	telefon string,
	stanowisko string,
	haslo string
);


CREATE TABLE Zamowienie (
	id_zamowienia integer,
	id_klienta integer,
	id_restauracji integer,
	kwota float,
	status string,
  oplacone boolean,
	data_dodania date,
  czas_dostawy integer,
  czas_realizacji integer,
  data_zlozenia date,
	ocena integer,
  miasto string,
  adres string
);

CREATE TABLE Danie (
  id_dania integer,
	id_restauracji integer,
	nazwa string,
	cena float,
	opis string
);


CREATE TABLE Restauracja (
	id_restauracji integer PRIMARY KEY AUTOINCREMENT,
	nazwa string,
	adres string
);


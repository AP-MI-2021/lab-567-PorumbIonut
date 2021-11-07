from Domain.rezervare import getCheckin, getClasa, getId, getNume, getPret
from Logic.CRUD import adaugaRezervare, getbyID, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "business", "120", "nu", lista)
    assert len(lista) == 1
    assert getId(getbyID("1", lista)) == "1"
    assert getNume(lista[0]) == "Porumb Ionut"
    assert getClasa(lista[0]) == "business"
    assert getPret(lista[0]) == "120"
    assert getCheckin(lista[0]) == "nu"


def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "business", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "business", "120", "nu", lista)

    lista = stergeRezervare("1", lista)
    assert len(lista) == 1
    assert getbyID("2", lista) is not None

def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "business", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "business", "120", "nu", lista)

    lista = modificaRezervare("1", "Porumb Ionut", "economy plus", "110", "da", lista)
    assert getClasa(lista[0]) == "economy plus"
    assert getPret(lista[0]) == "110"
    assert getNume(lista[0]) == "Porumb Ionut"

def testgetbyID():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "business", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "business", "120", "nu", lista)
    assert getbyID("1", lista) == [('id: ', '1'), ('nume: ', 'Porumb Ionut'), ('clasa: ', 'business'), ('pret: ', '120'), ('checkin: ', 'nu')]

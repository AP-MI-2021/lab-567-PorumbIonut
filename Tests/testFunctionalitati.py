from Logic.CRUD import adaugaRezervare
from Logic.functionalitati import ieftinireRezervari, pretMaximPentruFiecareClasa, ordonareDescrescatoareDupaPret, \
    sumePentruFiecareNume, trecereRezervareLaClasaSuperioara


def testTrecereRezervareLaClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "economy plus", "100", "da", lista)
    lista = adaugaRezervare("3", "Bogdan", "economy", "100", "da", lista)
    assert trecereRezervareLaClasaSuperioara("Bogdan",lista) == [[('id: ', '1'), ('nume: ', 'Porumb Ionut'), ('clasa: ', 'economy'), ('pret: ', '120'), ('checkin: ', 'nu')], [('id: ', '2'), ('nume: ', 'Bogdan'), ('clasa: ', 'business'), ('pret: ', '100'), ('checkin: ', 'da')], [('id: ', '3'), ('nume: ', 'Bogdan'), ('clasa: ', 'economy plus'), ('pret: ', '100'), ('checkin: ', 'da')]]
#testTrecereRezervareLaClasaSuperioara()
def testIeftiniri():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "business", "100", "da", lista)
    assert ieftinireRezervari(lista, 20) ==[[('id: ', '1'), ('nume: ', 'Porumb Ionut'), ('clasa: ', 'economy'), ('pret: ', '120'), ('checkin: ', 'nu')], [('id: ', '2'), ('nume: ', 'Bogdan'), ('clasa: ', 'business'), ('pret: ', 80.0), ('checkin: ', 'da')]]

#testIeftiniri()
def testPretMaximPentruFiecareClasa():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "business", "100", "da", lista)
    assert pretMaximPentruFiecareClasa(lista) == (120, 0, 100)

#testPretMaximPentruFiecareClasa()

def testOrdonareDescrescatoareDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "business", "150", "da", lista)
    assert ordonareDescrescatoareDupaPret(lista) == [[('id: ', '2'), ('nume: ', 'Bogdan'), ('clasa: ', 'business'), ('pret: ', '150'), ('checkin: ', 'da')], [('id: ', '1'), ('nume: ', 'Porumb Ionut'), ('clasa: ', 'economy'), ('pret: ', '120'), ('checkin: ', 'nu')]]
#testOrdonareDescrescatoareDupaPret()

def testSumePentruFiecareNume():
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "business", "150", "da", lista)
    lista = adaugaRezervare("3", "Porumb Ionut", "business", "150", "nu", lista)
    assert sumePentruFiecareNume(lista) == {'Porumb Ionut': 270.0, 'Bogdan': 150.0}

#testSumePentruFiecareNume()
from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Porumb Ionut", "business", "120", "nu", lista)
    lista = adaugaRezervare("2", "Bogdan", "economy", "100", "da", lista)
    runMenu(lista)

main()
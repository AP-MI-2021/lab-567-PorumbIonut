from Domain.rezervare import toString
from Logic.CRUD import  stergeRezervare, modificaRezervare, adaugaRezervare
from Logic.functionalitati import trecereRezervareLaClasaSuperioara, ieftinireRezervari


def printMenu():
    print("1.Adauga rezervare")
    print("2.Sterge rezervare")
    print("3.Modifica rezervare")
    print("4.Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5.Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("a.Afiseaza toate rezervarile")
    print("x.Inchide meniul")


def uiAdaugaRezervare(lista):
    id = input("dati id: ")
    nume = input("dati nume: ")
    clasa = input("dati clasa: ")
    pret = float(input("dati pret: "))
    checkin = input("ati facut checkin-ul?: ")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)

def uiStergeRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return stergeRezervare(id, lista)

def uiModificaRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = input("Dati pretul: ")
    checkin = input("Checkin: ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def uiUpgradeazaClasa(lista):
    nume = input("Dati numele pentru care vreti sa upgradati clasa: ")
    return trecereRezervareLaClasaSuperioara(nume, lista)

def uiIeftinireRezervari(lista):
    procent = int(input("Dati procentajul care va fi aplicat pentru ieftinirea rezervarilor care au checkin facut: "))
    return ieftinireRezervari(lista, procent)

def runMenu(lista):
    while True:
        printMenu()
        option = input("Dati optiunea: ")
        if option == "1":
            lista = uiAdaugaRezervare(lista)
        elif option == "2":
            lista = uiStergeRezervare(lista)
        elif option == "3":
            lista = uiModificaRezervare(lista)
        elif option == "4":
            lista = uiUpgradeazaClasa(lista)
        elif option == "5":
            lista = uiIeftinireRezervari(lista)
        elif option == "a":
            showAll(lista)
        elif option == "x":
            break
        else:
            print("Optiune gresita! Reincercati")




from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.command_line_console import runMenu2
from UI.console import runMenu

def optiuni():
    print("1.Alege meniul standard")
    print("2.Alege meniul in care poti apela mai multe functii in acelasi timp!")

def main():
    runAllTests()
    lista = []
    optiuni()
    optiune = input("Alege main-ul pe care vrei sa-l rulezi: ")
    if optiune == "1":
        runMenu(lista)
    elif optiune == "2":
        runMenu2(lista)
    else:
        print("Meniul selectat nu exista! Reincercati! ")

main()
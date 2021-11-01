from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.command_line_console import runMenu2
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    #runMenu(lista)
    runMenu2(lista)
main()
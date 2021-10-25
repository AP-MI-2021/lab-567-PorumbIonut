from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare, testgetbyID
from Tests.testDomeniu import testRezervare


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testgetbyID()
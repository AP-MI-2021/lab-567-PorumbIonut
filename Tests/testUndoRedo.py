from Logic.CRUD import adaugaRezervare, modificaRezervare, stergeRezervare


def testUndoRedo():
    undolst = []
    redolst = []
    lista = []
    undolst.append(lista)
    redolst.clear()
    lista = adaugaRezervare("1", "porumb", "economy", 100, "da", lista)
    # undo
    redolst.append(lista)
    lista = undolst.pop()
    assert lista == []
    # redo
    undolst.append(lista)
    lista = redolst.pop()
    assert lista == [
        [("id: ", "1"), ("nume: ", "porumb"), ("clasa: ", "economy"), ("pret: ", 100), ("checkin: ", "da")]]

    undolst.append(lista)
    redolst.clear()
    lista = adaugaRezervare("2", "bogdan", "economy plus", 110, "nu", lista)
    # undo
    redolst.append(lista)
    lista = undolst.pop()
    assert lista == [
        [("id: ", "1"), ("nume: ", "porumb"), ("clasa: ", "economy"), ("pret: ", 100), ("checkin: ", "da")]]

    # redo
    undolst.append(lista)
    lista = redolst.pop()

    assert lista == [
        [("id: ", "1"), ("nume: ", "porumb"), ("clasa: ", "economy"), ("pret: ", 100), ("checkin: ", "da")],
        [("id: ", "2"), ("nume: ", "bogdan"), ("clasa: ", "economy plus"), ("pret: ", 110), ("checkin: ", "nu")]]

    undolst.append(lista)
    redolst.clear()

    lista = modificaRezervare("1", "porumb", "business", 120, "da", lista)

    # undo
    redolst.append(lista)
    lista = undolst.pop()
    assert lista == [
        [("id: ", "1"), ("nume: ", "porumb"), ("clasa: ", "economy"), ("pret: ", 100), ("checkin: ", "da")],
        [("id: ", "2"), ("nume: ", "bogdan"), ("clasa: ", "economy plus"), ("pret: ", 110), ("checkin: ", "nu")]]

    # redo
    undolst.append(lista)
    lista = redolst.pop()

    undolst.append(lista)
    redolst.clear()

    lista = stergeRezervare("2", lista)
    assert lista == [
        [("id: ", "1"), ("nume: ", "porumb"), ("clasa: ", "business"), ("pret: ", 120), ("checkin: ", "da")]]

    # undo
    redolst.append(lista)
    lista = undolst.pop()

    assert lista == [
        [("id: ", "1"), ("nume: ", "porumb"), ("clasa: ", "business"), ("pret: ", 120), ("checkin: ", "da")],
        [("id: ", "2"), ("nume: ", "bogdan"), ("clasa: ", "economy plus"), ("pret: ", 110), ("checkin: ", "nu")]]

    # redo
    undolst.append(lista)
    lista = redolst.pop()
    assert lista == [
        [("id: ", "1"), ("nume: ", "porumb"), ("clasa: ", "business"), ("pret: ", 120), ("checkin: ", "da")]]


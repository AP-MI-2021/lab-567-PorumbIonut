def creeaza_rezervare(id, nume, clasa, pret, checkin):
    # creeaza o rezervare si returneaza un dictionar ce retine rezervarea facuta
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }


def getId(rezervare):
    return rezervare["id"]


def getNume(rezervare):
    return rezervare["nume"]


def getClasa(rezervare):
    return rezervare["clasa"]


def getPret(rezervare):
    return rezervare["pret"]


def getCheckin(rezervare):
    return rezervare["checkin"]


def toString(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )

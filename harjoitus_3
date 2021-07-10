def random_number():
    import random

    vuosi = random.randint(1900, 2000)
    return vuosi

random_number()


def random_name():
    import random
    import string

    kirjaimet = string.ascii_lowercase
    nimi = ''.join(random.choice(kirjaimet) for i in range(10))
    return nimi

random_name()


def main():
    import sqlite3
    import time

    db = sqlite3.connect("testi.db")
    db.isolation_level = None

    db.execute("BEGIN")

    # luodaan taulu
    db.execute("DROP TABLE IF EXISTS Elokuvat")
    db.execute("CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")

    # otetaan aika alusta talteen
    alku = time.time()

    # lisä?tä?ä?n tauluun random tiedot
    for i in range(0, 1000000):
        nimi = random_name()
        vuosi = random_number()
        db.execute("INSERT INTO Elokuvat (nimi, vuosi) VALUES (?, ?)", [nimi, vuosi])

    db.execute("COMMIT")
    # otetaan rivien lisä?ä?misen aika talteen
    rivit_aika = time.time()

    # lisä?tä?ä?n indeksi
    db.execute("CREATE INDEX idx_vuosi ON Elokuvat (vuosi)")
    
    # rivien hakeminen ilman indeksiä?
    for j in range(0, 1000):
        vuosi = random_number()
        db.execute("SELECT COUNT(*) FROM Elokuvat WHERE vuosi=?", [vuosi]).fetchall()

    # otetaan kyselyihin mennyt aika talteen
    kyselyt_aika = time.time()

    print(rivit_aika - alku)
    print(kyselyt_aika - alku)


main()

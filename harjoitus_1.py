def main():
    import sqlite3

    db = sqlite3.connect("kurssit_1.db")
    db.isolation_level = None

    while True:
        toiminto = int(input("Valitse toiminto: "))

        # Lasketaan annettuna vuonna saatujen opintopisteiden yhteismä?ä?rä?
        if toiminto == 1:
            vuosi = input("Valitse vuosi: ")
            vuosi = vuosi+"%"
            pisteet = db.execute("""SELECT SUM(K.laajuus) FROM Suoritukset S, Kurssit K
                                 WHERE K.id = S.kurssi_id AND S.paivays
                                 LIKE ?""", [vuosi]).fetchall()
            for piste in pisteet:
                print(piste[0])

        # Tulostetaan annetun opiskelijan kaikki suoritukset aikajä?rjestyksessä?
        if toiminto == 2:
            nimi = input("Anna opiskelijan nimi: ")
            suoritukset = db.execute("""SELECT K.nimi, K.laajuus, S.paivays, S.arvosana 
                                        FROM Suoritukset S, Opiskelijat O, Kurssit K 
                                        WHERE O.id = S.opiskelija_id 
                                        AND K.id = S.kurssi_id AND O.nimi = ?
                                        GROUP BY K.id
                                        ORDER BY S.paivays""", [nimi]).fetchall()

            print("kurssi         op   pä?ivä?ys        arvosana")

            for suoritus in suoritukset:
                if suoritus[1] >= 10:
                    print(suoritus[0], "       ", suoritus[1], "    ", suoritus[2], "     ", suoritus[3])
                else:
                    print(suoritus[0], "        ", suoritus[1], "    ", suoritus[2], "     ", suoritus[3])

        # Tulostetaan annetun kurssin suoritusten arvosanojen jakauma
        if toiminto == 3:
            kurssi = input("Anna kurssin nimi: ")
            arvosanat = db.execute("""SELECT S.arvosana, COUNT(S.arvosana) 
                                   FROM Suoritukset S, Kurssit K 
                                   WHERE K.id = S.kurssi_id AND K.nimi = ?
                                   GROUP BY arvosana""", [kurssi]).fetchall()

            for arvosana in arvosanat:
                print("Arvosana ", arvosana[0], ": ", arvosana[1], " kpl", sep="")

        # Tulostetaan top X-mä?ä?rä? eniten opintopisteitä? antaneet opettajat
        if toiminto == 4:
            opettaja_kpl = int(input("Anna opettajien mä?ä?rä?: "))
            opettajat = db.execute("""SELECT O.nimi, SUM(K.laajuus) 
                                    FROM Opettajat O, Kurssit K, Suoritukset S 
                                    WHERE O.id = K.opettaja_id AND S.kurssi_id = K.id 
                                    GROUP BY O.id ORDER BY SUM(K.laajuus) DESC
                                    LIMIT ?""", [opettaja_kpl]).fetchall()

            for opettaja in opettajat:
                print("{:20s}".format(opettaja[0]), "{:5d}".format(opettaja[1]))

        # Suljetaan ohjelma
        if toiminto == 5:
           break

main()

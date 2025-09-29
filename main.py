import random
import mysql.connector
import tarina

#SQL yhteys
yhteys = mysql.connector.connect(
    host='localhost',
    port=3307,
    database='flight_game',
    user='root',
    password='mikasana',
    autocommit=True
)

#Kysymys -funktio
def kysymysfunktio(i):
    # Sanakirja, johon vastaukset talletetaan
    vastauslista = {}

    # Lista joka asettaa oikeat ja väärät vastaukset satunnaiseen järjestykseen
    random_lista = ["1", "2", "3", "4"]
    random.shuffle(random_lista)

    if i < 6:
        #Luodaan helppokysymys

        #Haetaan kysymykseen muuttuja
        sql = f"SELECT name, ident FROM airport ORDER BY RAND() LIMIT 1"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        #Haun tulos muuttujaan
        kysymys = kursori.fetchone()

        #Haetaan kysymykseen vastaus
        sql = f"SELECT name, iso_country FROM country WHERE iso_country in(SELECT iso_country FROM airport WHERE ident = '{kysymys[1]}')"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        #Oikea vastaus muuttujaan
        oikea_vastaus = kursori.fetchone()

        #Haetaan 3 väärää vastausta
        sql = f"SELECT name FROM country WHERE NOT iso_country = '{oikea_vastaus[1]}' ORDER BY RAND() LIMIT 3"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        #Väärät vastaukset muuttujaan
        vaarat_vastaukset = kursori.fetchall()

        #Luodaan vastauslista, jossa vastauksen järjestys määräytyy random_listan mukaan
        vastauslista[f"vastaus{random_lista[0]}"] = oikea_vastaus[0], 1
        vastauslista[f"vastaus{random_lista[1]}"] = vaarat_vastaukset[0][0], 0
        vastauslista[f"vastaus{random_lista[2]}"] = vaarat_vastaukset[1][0], 0
        vastauslista[f"vastaus{random_lista[3]}"] = vaarat_vastaukset[2][0], 0
    elif i < 11:
        #Luodaan keskivaikea kysymys

        # Haetaan kysymykseen muuttuja
        sql = f"SELECT name, ident FROM airport ORDER BY RAND() LIMIT 1"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        # Haun tulos muuttujaan
        kysymys = kursori.fetchone()

        # Haetaan kysymykseen vastaus
        sql = f"SELECT ident FROM airport WHERE ident = '{kysymys[1]}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        # Oikea vastaus muuttujaan
        oikea_vastaus = kursori.fetchone()

        # Haetaan 3 väärää vastausta
        sql = f"SELECT ident FROM airport WHERE NOT ident = '{oikea_vastaus[0]}' ORDER BY RAND() LIMIT 3"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        # Väärät vastaukset muuttujaan
        vaarat_vastaukset = kursori.fetchall()

        # Luodaan vastauslista, jossa vastauksen järjestys määräytyy random_listan mukaan
        vastauslista[f"vastaus{random_lista[0]}"] = oikea_vastaus[0], 1
        vastauslista[f"vastaus{random_lista[1]}"] = vaarat_vastaukset[0][0], 0
        vastauslista[f"vastaus{random_lista[2]}"] = vaarat_vastaukset[1][0], 0
        vastauslista[f"vastaus{random_lista[3]}"] = vaarat_vastaukset[2][0], 0

    elif i < 16:
        #Luodaan vaikea kysymys

        # Haetaan kysymykseen muuttuja
        sql = f"SELECT ident FROM airport ORDER BY RAND() LIMIT 1"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        # Haun tulos muuttujaan
        kysymys = kursori.fetchone()

        # Haetaan kysymykseen vastaus
        sql = f"SELECT name FROM airport WHERE ident = '{kysymys[0]}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        # Oikea vastaus muuttujaan
        oikea_vastaus = kursori.fetchone()

        # Haetaan 3 väärää vastausta
        sql = f"SELECT name FROM airport WHERE NOT ident = '{kysymys[0]}' ORDER BY RAND() LIMIT 3"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        # Väärät vastaukset muuttujaan
        vaarat_vastaukset = kursori.fetchall()

        # Luodaan vastauslista, jossa vastauksen järjestys määräytyy random_listan mukaan
        vastauslista[f"vastaus{random_lista[0]}"] = oikea_vastaus[0], 1
        vastauslista[f"vastaus{random_lista[1]}"] = vaarat_vastaukset[0][0], 0
        vastauslista[f"vastaus{random_lista[2]}"] = vaarat_vastaukset[1][0], 0
        vastauslista[f"vastaus{random_lista[3]}"] = vaarat_vastaukset[2][0], 0
    else:
        #Voittaja
        return "winner"

    # Palautetaan funktiosta sanakirja, joka sisältää kysymyksen, vastaukset ja tiedon onko vastaus oikein vai väärin
    return {
        "vastaus1": ["A", vastauslista["vastaus1"][0], vastauslista["vastaus1"][1]],
        "vastaus2": ["B", vastauslista["vastaus2"][0], vastauslista["vastaus2"][1]],
        "vastaus3": ["C", vastauslista["vastaus3"][0], vastauslista["vastaus3"][1]],
        "vastaus4": ["D", vastauslista["vastaus4"][0], vastauslista["vastaus4"][1]],
        "kysymys": kysymys[0]
    }

#High Score -funktio
def highscore():
    #Haetaan pelaajien nimet ja pisteet taulusta, järjestetään ne ja rajoitetaan vain 10 parhaaseen tulokseen
    sql = f"SELECT name, score FROM highscores ORDER BY score DESC LIMIT 10"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    #Printataan jokainen rivi
    for rivi in tulos:
        print(f"Name: {rivi[0]}, Score: {rivi[1]}")
    return

#Score Insert -funktio
def scoreinsert(username, money):
    mycursor = yhteys.cursor()
    #Lisätään pelaajan nimi ja pisteet highscores -tauluun
    sql = f"INSERT INTO highscores (name, score) VALUES (%s, %s)"
    val = (username, money)
    mycursor.execute(sql, val)
    yhteys.commit()


def oljenkorret(kysymys_sanakirja, olki1, olki2, olki3):
    print("\nLifelines:")
    if olki1 == False:
        print("1. Ask the audience")
    if olki2 == False:
        print("2. Eliminate 2 wrong answers")
    if olki3 == False:
        print("3. Call a friend")
    valinta = input("Choose a lifeline (1/2/3): ")

    if valinta == "1":
        olki1 = True
        # Kysy yleisöltä
        yleison_mielipide = {
            "A": random.randint(0, 60),
            "B": random.randint(0, 60),
            "C": random.randint(0, 60),
            "D": random.randint(0, 60),
        }
        oikea_vastaus_kirjain = ""
        for i in kysymys_sanakirja:
            if kysymys_sanakirja[i][2] == 1:
                oikea_vastaus_kirjain = kysymys_sanakirja[i][0]
                break

        yleison_mielipide[oikea_vastaus_kirjain] = random.randint(40,90)

        print("\nAudience thinks it is:")
        for kirjain, prosentti in yleison_mielipide.items():
            if kirjain == "A":
                print(f"A: {prosentti}%")
            elif kirjain == "B":
                print(f"B: {prosentti}%")
            elif kirjain == "C":
                print(f"C: {prosentti}%")
            elif kirjain == "D":
                print(f"D: {prosentti}%")

    elif valinta == "2":
        olki2 = True
        oikea_vastaus_kirjain = ""
        for i in kysymys_sanakirja:
            if kysymys_sanakirja[i][2] == 1:
                oikea_vastaus_kirjain = i
                break

        poistettavat_kirjaimet = []
        for kirjain in kysymys_sanakirja:
            if kirjain != "kysymys":
                if kirjain != oikea_vastaus_kirjain:
                    poistettavat_kirjaimet.append(kirjain)

        poistettavat_kirjaimet = random.sample(poistettavat_kirjaimet, 2)

        print("\n2 wrong answers have been eliminated:")
        for kirjain in kysymys_sanakirja:
            if kirjain not in poistettavat_kirjaimet:
                if kirjain == "vastaus1":
                    print(f"A: {kysymys_sanakirja["vastaus1"][1]}")
                elif kirjain == "vastaus2":
                    print(f"B: {kysymys_sanakirja["vastaus2"][1]}")
                elif kirjain == "vastaus3":
                    print(f"C: {kysymys_sanakirja["vastaus3"][1]}")
                elif kirjain == "vastaus4":
                    print(f"D: {kysymys_sanakirja["vastaus4"][1]}")

    elif valinta == "3":
        olki3 = True
        # Soita kaverille
        kaverin_vastaus = ""
        for i in kysymys_sanakirja:
            if kysymys_sanakirja[i][2] == 1:
                kaverin_vastaus = kysymys_sanakirja[i][1]
                break
        print("\nFriends answer:")
        print(f"I think the answer is: {kaverin_vastaus}")
    else:
        print("Incorrect input.")

    return kysymys_sanakirja, olki1, olki2, olki3


#Peliprosessi
def game():
    # Muuttuja joka määrittää kysytäänkö kysymyksiä
    game_over = False
    olki1 = False
    olki2 = False
    olki3 = False

    # Pelaajan raha ja edistyminen
    money = 0
    current_round = 0

    while game_over == False:
        #Alkuteksti
        for line in tarina.getStory():
            print(line)
        print("Type [START] to start the game.")
        print("Type [SCORES] to see the highscores.")
        valinta = input("[START]/[SCORES]: ").upper()

        #Tulostetaan high score -taulu
        while valinta == "SCORES":
            highscore()
            valinta = input("[START]/[SCORES]: ").upper()

        #Pelin käynnistys
        if valinta == "START":
            username = input('Enter your username: ')

            #Haetaan kysymys-sanakirja
            current_round = 1
            while current_round < 17:
                kysymys_sanakirja = kysymysfunktio(current_round)

                if kysymys_sanakirja == "winner":
                    print("You won!")
                    break
                else:
                    print(kysymys_sanakirja)
                    print(kysymys_sanakirja["kysymys"])
                    print(f"{kysymys_sanakirja["vastaus1"][0]}. {kysymys_sanakirja["vastaus1"][1]}")
                    print(f"{kysymys_sanakirja["vastaus2"][0]}. {kysymys_sanakirja["vastaus2"][1]}")
                    print(f"{kysymys_sanakirja["vastaus3"][0]}. {kysymys_sanakirja["vastaus3"][1]}")
                    print(f"{kysymys_sanakirja["vastaus4"][0]}. {kysymys_sanakirja["vastaus4"][1]}")
                    if olki1 == False or olki2 == False or olki3 == False:
                        print(f"E. Use a lifeline")

                    #Vastauskenttä
                    vastaus = input('Enter your answer: ').upper()

                    if vastaus == kysymys_sanakirja["vastaus1"][0]:
                        if kysymys_sanakirja["vastaus1"][2] == 1:
                            print("This answer is correct!")
                            current_round += 1
                        else:
                            print("This answer is incorrect!")
                            break
                    elif vastaus == kysymys_sanakirja["vastaus2"][0]:
                        if kysymys_sanakirja["vastaus2"][2] == 1:
                            print("This answer is correct!")
                            current_round += 1
                        else:
                            print("This answer is incorrect!")
                            break
                    elif vastaus == kysymys_sanakirja["vastaus3"][0]:
                        if kysymys_sanakirja["vastaus3"][2] == 1:
                            print("This answer is correct!")
                            current_round += 1
                        else:
                            print("This answer is incorrect!")
                            break
                    elif vastaus == kysymys_sanakirja["vastaus4"][0]:
                        if kysymys_sanakirja["vastaus4"][2] == 1:
                            print("This answer is correct!")
                            current_round += 1
                        else:
                            print("This answer is incorrect!")
                            break
                    elif vastaus == "E":
                        if olki1 == True & olki2 == True & olki3 == True:
                            print("Incorrect input; you have no lifelines.")
                            break
                        else:
                            kysymys_sanakirja, olki1, olki2, olki3 = oljenkorret(kysymys_sanakirja, olki1, olki2, olki3)
                            print(kysymys_sanakirja)
                            vastaus = input('Enter your answer: ').upper()
                            if vastaus == kysymys_sanakirja["vastaus1"][0]:
                                if kysymys_sanakirja["vastaus1"][2] == 1:
                                    print("This answer is correct!")
                                    current_round += 1
                                else:
                                    print("This answer is incorrect!")
                                    break
                            elif vastaus == kysymys_sanakirja["vastaus2"][0]:
                                if kysymys_sanakirja["vastaus2"][2] == 1:
                                    print("This answer is correct!")
                                    current_round += 1
                                else:
                                    print("This answer is incorrect!")
                                    break
                            elif vastaus == kysymys_sanakirja["vastaus3"][0]:
                                if kysymys_sanakirja["vastaus3"][2] == 1:
                                    print("This answer is correct!")
                                    current_round += 1
                                else:
                                    print("This answer is incorrect!")
                                    break
                            elif vastaus == kysymys_sanakirja["vastaus4"][0]:
                                if kysymys_sanakirja["vastaus4"][2] == 1:
                                    print("This answer is correct!")
                                    current_round += 1
                                else:
                                    print("This answer is incorrect!")
                                    break
                            else:
                                print("Invalid answer!")
                                break

                    else:
                        print("Invalid answer!")
                        break
            break
        game_over = True

    #Palataan pois funktiosta
    return username, money

#Aloitetaan peli-funktio, joka palauttaa käyttäjänimen ja pisteet muuttujaan
score = game()
#Lisätään tiedot tietokantaan
scoreinsert(score[0], score[1])

#Kysytään haluaako pelaaja käynnistää pelin uudelleen
print("GAME OVER!")
restart = input('Do you want to try again? (y/n): ').upper()
if restart == 'Y':
    game()
elif restart == 'N':
    exit()


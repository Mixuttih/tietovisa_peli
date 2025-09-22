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

#Peliprosessi
def game():
    # Muuttuja joka määrittää kysytäänkö kysymyksiä
    game_over = False

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

            #Esimerkki-kysymys
            print("This is a question?")
            print("A. This is correct")
            print("B. This in incorrect")
            print("C. This is incorrect")
            print("D. This is incorrect")

            #Vastauskenttä
            vastaus = input('Enter your answer: ').upper()
            if vastaus == 'A':
                print("This answer is correct!")
                break
            elif vastaus == 'B':
                print("This answer is incorrect!")
                game_over = True
            elif vastaus == 'C':
                print("This answer is incorrect!")
                game_over = True
            elif vastaus == 'D':
                print("This answer is incorrect!")
                game_over = True
            else:
                print("Invalid answer!")
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


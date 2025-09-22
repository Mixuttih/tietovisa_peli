import random
import mysql.connector

#SQL yhteys
yhteys = mysql.connector.connect(
    host='localhost',
    port=3307,
    database='flight_game',
    user='root',
    password='mikasana',
    autocommit=True
)

def game():
    # Muuttuja joka määrittää kysytäänkö kysymyksiä
    game_over = False

    # Pelaajan raha ja edistyminen
    money = 0
    current_round = 0

    while game_over == False:
        #Alkuteksti
        print("Welcome to 'Whomst would liketh to be a Big Money Person?'!")
        print("Type [START] to start the game.")
        print("Type [SCORES] to see the highscores.")
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
            vastaus = input('Enter your answer: ')
            if vastaus == 'A':
                print("This answer is correct!")
            elif vastaus == 'B':
                print("This answer is incorrect!")
                game_over = True
            elif vastaus == 'C':
                print("This answer is incorrect!")
                game_over = True
            elif vastaus == 'D':
                print("This answer is incorrect!")
                game_over = True
    #Palataan pois funktiosta
    return

#Aloitetaan peli
game()

#Kysytään haluaako pelaaja käynnistää pelin uudelleen
restart = input('Do you want to try again? (y/n): ').upper()
if restart == 'Y':
    game()
elif restart == 'N':
    exit()


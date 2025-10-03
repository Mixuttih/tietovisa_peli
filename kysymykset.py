import random
import mysql.connector
import tarina
from geopy import distance

#SQL yhteys
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Sorsalampi2025',
    autocommit=True
)

'''# Which country is airport x located?
sql1 = f"SELECT name, ident FROM airport ORDER BY RAND() LIMIT 1"
sql2 = f"SELECT name, iso_country FROM country WHERE iso_country in(SELECT iso_country FROM airport WHERE ident = '{sql1}')"
sql3 = f"SELECT name FROM country WHERE NOT iso_country = '{sql2}' ORDER BY RAND() LIMIT 3"

# How high is x airport?
sql4 = f"SELECT name, ident FROM airport ORDER BY RAND() LIMIT 1"
sql5 = f"SELECT elevation_ft*0.3048 as elevation_m FROM airport WHERE ident = '{sql4}'"
sql6 = f"SELECT elevation_ft*0.3048 as elevation_m FROM airport WHERE NOT ident = '{sql5}' ORDER BY RAND() LIMIT 3"

# What is x airport's gps-code?
sql7 = f"SELECT name, ident FROM airport ORDER BY RAND() LIMIT 1"
sql8 = f"SELECT gps_code FROM airport WHERE ident = '{sql7}'"
sql9 = f"SELECT gps_code FROM airport WHERE NOT ident = '{sql8}' ORDER BY RAND() LIMIT 3"

# What is a distance between x and x airport?
kysymys = print

def get_random_airports():
    sql10 = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport ORDER BY RAND() LIMIT 2"
    cursor = yhteys.cursor()
    cursor.execute(sql10)
    result = cursor.fetchall()
    return result[0], result[1]

print(get_random_airports())

def specific_distance(result):
    result1, result2 = result
    name1, ident1, latitude1, longitude1 = result1
    name2, ident2, latitude2, longitude2 = result2
    return distance.distance((latitude1, longitude1),
                                (latitude2, longitude2))

#print(specific_distance())
    #menee monimutkaiseksi ei voi nimetä result suoraan
print("-------------------------------------------")
sql10 = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport ORDER BY RAND() LIMIT 2"

def spesific_distance():
    sql11 = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport WHERE idet = '{sql10}"
    cursor = yhteys.cursor()
    cursor.execute(sql10)
    result = cursor.fetchall()
    name1, ident1, latitude1, longitude1 = result[0]
    name2, ident2, latitude2, longitude2 = result[1]
    return result[0], result[1], distance.distance((latitude1, longitude1),
                             (latitude2, longitude2))
print(spesific_distance())

def random_distance():
    sql10 = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport ORDER BY RAND() LIMIT 2"
    cursor = yhteys.cursor()
    cursor.execute(sql10)
    result = cursor.fetchall()
    name1, ident1, latitude1, longitude1 = result[0]
    name2, ident2, latitude2, longitude2 = result[1]
    return result[0], result[1], distance.distance((latitude1, longitude1),
                             (latitude2, longitude2))

#print(random_distance())



sql11 = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport ORDER BY RAND() LIMIT 6"

# get airport info
def get_airport_info(icao):
    sql = f'SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result''''''

# calculate distance between two airports
def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km


print(get_airport_info)

'''

# How much CO2 emissions does flight from x airport to x airport produce?

if kysymysvalinta == 5:
    question_text = ["How much CO2 emmission are produced on a flight between ", " airports on Airbus A320?"]
    # Haetaan kysymykseen muuttujat
    sql = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport ORDER BY RAND() LIMIT 2"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    kysymys = kursori.fetchall()

    # Lasketaan kahden haetun lentokentän etäisyys
    start = [kysymys[0][2], kysymys[0][3]]
    end = [kysymys[1][2], kysymys[1][3]]

    print(start)
    print(end)
    # Oikea vastaus palautetaan kokonaislukuna
    oikea_vastaus = [int(distance.distance((start[0], start[1]), (end[0], end[1])).km)] * 9.2
    kg / km

    # Luodaan random luvut vääriksi vastauksiksi
    vaarat_vastaukset = [random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000)] * 9.2
    kg / km

    # Luodaan vastauslista, jossa vastauksen järjestys määräytyy random_listan mukaan
    vastauslista[f"vastaus{random_lista[0]}"] = oikea_vastaus[0], 1
    vastauslista[f"vastaus{random_lista[1]}"] = vaarat_vastaukset[0], 0
    vastauslista[f"vastaus{random_lista[2]}"] = vaarat_vastaukset[1], 0
    vastauslista[f"vastaus{random_lista[3]}"] = vaarat_vastaukset[2], 0


# Which is highest airport from sea level?
sql13 = f" SELECT name, ident, MAX(elevation_ft)*0.3048 as elevation_m FROM airport"
cursor = yhteys.cursor()
cursor.execute(sql13)
kysymys = cursor.fetchone()
print(kysymys)

#Which is lowest airport from sea level?
sql14 = f"SELECT name, ident, MIN(elevation_ft)*0.3048 as elevation_m FROM airport"
cursor.execute(sql14)
kysymys2 = cursor.fetchone()
print(kysymys2)'''

#Which airport is most uneconomical airport you can fly to from helsinki-vantaa airport?

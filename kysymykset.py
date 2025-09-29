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

# Which country is airport x located?
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
sql10 = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport ORDER BY RAND() LIMIT 2"
sql11 = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport ORDER BY RAND() LIMIT 5"

# get airport info
def get_airport_info(icao):
    sql = f'''SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result

# calculate distance between two airports
def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km



# How much CO2 emissions does flight from x airport to x airport produce?


# Which is highest airport from sea level?

# Which is lowest airport from sea level?

# Which airport is most uneconomical airport you can fly to from helsinki-vantaa airport?
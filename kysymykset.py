
# Which country is airport x located?
sql1 = f"SELECT name, ident FROM airport ORDER BY RAND() LIMIT 1"
sql2 = f"SELECT name, iso_country FROM country WHERE iso_country in(SELECT iso_country FROM airport WHERE ident = '{kysymys[1]}')"
sql3 = f"SELECT name FROM country WHERE NOT iso_country = '{oikea_vastaus[1]}' ORDER BY RAND() LIMIT 3"

# How high is x airport?
sql4 = f"SELECT name FROM airport ORDER BY RAND() LIMIT 1"
sql5 = f"SELECT elevation_ft*0.3048 as elevation_m FROM airport WHERE name = '{kysymys[2]}'"
sql6 = f"SELECT elevation_ft*0.3048 as elevation_m FROM airport WHERE NOT name = '{oikea_vastaus[2]' ORDER BY RAND() LIMIT 3"
# What is a distance between x and x airport?

# How much CO2 emissions does flight from x airport to x airport produce?

# What is x airport's gps-code?

# Which is highest airport from sea level?

# Which is lowest airport from sea level?

# Which airport is most uneconomical airport you can fly to from helsinki-vantaa airport?
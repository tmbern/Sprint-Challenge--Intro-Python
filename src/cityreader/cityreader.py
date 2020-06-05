import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
    def __init__(self, name, lat, lon):
      self.name = name
      self.lat = lat
      self.lon = lon
    
    def __str__(self):
        return f'Name: {self.name}, Lat: {self.lat}, Lon: {self.lon}'

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    with open('src/cityreader/cities.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        # loop through the CSV and populate the list with the City Instances
        for line in csvreader:
            cities.append(City(name=line['city'], lat=float(line['lat']), lon=float(line['lng'])))

    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)





import time
print('----'*14)
# get the input from the user. We want it to be comma seperated so we can the inputs as seperate int. 
lat_lon1 = input('enter a latitude and longitude in the form of 45, -100: ')
time.sleep(1.5)
lat_lon2 = input('enter another latitude and longitude in the form of 32, -120: ')

# split the inputs so we have a list that we can index. 
coordinate1 = lat_lon1.split()
coordinate2 = lat_lon2.split()

# index the coordinates to get the individual lat and lon that we will pass to the function.
lat1 = int(coordinate1[0].strip(','))
lon1 = int(coordinate1[1].strip(','))
lat2 = int(coordinate2[0].strip(','))
lon2 = int(coordinate2[1].strip(','))

within = []

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
    for i in cities:
        if (i.lat <= max(lat1, lat2) and i.lat >= min(lat1, lat2)) and (i.lon <= max(lon1, lon2) and i.lon >= min(lon1, lon2)):
            within.append(i)

    return within

# need logic to ensure that the input from the user is correct format. 
if len(coordinate1) == 2 and len(coordinate2) == 2:
    cityreader_stretch(lat1=lat1, lon1=lon1, lat2=lat2, lon2=lon2, cities=cities)
    for c in within:
      print(c)
else:
    print('that is not a valid input')

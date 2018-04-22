"""
    Author: "Javier Gombao Fernandez-Calvillo"
    eMail: a00248414@student.ait.ie
    College: Athlone Institute of Technology (AIT)
    Subject: Final Project
    File: generateMap.py
    
    The purpose of this script is to obtain all the names of the countries which IntelMQ has detected as a cyber threat
    Variables (lists):
    nameCountries: it provides the name if the country. Examples: Ireland, Spain, England, France...
    values: it defines the number of times which the country apperars in the result file given by IntelMQ
    latitude: it defines the latitude value
    longitude: it defines the longitude value
"""

# Import modules
import folium
import pandas as pd
import matplotlib.pyplot as plt

# Variables which we are going to use in the program
FILEOUTPUT = "output.txt"
countries = []
nameCountries =[]
values = []
latitude = []
longitude = []

# Set ipython's max row display
pd.set_option('display.max_row', 245)

"""This is a struct which defines the code of the country and its ocurrences"""
class Country():
    def __init__(self, country, count):
        self.country = country
        self.count = count
        self.latitude = latitude
        self.longitude = longitude

class Map(object):
    
    """Constructor of the function"""
    def __init__(self, fileEvents, fileCodeISOCountries):
        self._fileEvents=fileEvents
        self._fileCodeISOCountries=fileCodeISOCountries
    
    """It returns the name of the fileEvents"""
    def getFileEvents(self):
        return self._fileEvents
    
    """It gets the file with the name of the countries and their longitude and latitude (geolocation)"""
    def getFileCodeISOCountries(self):
        return self._fileCodeISOCountries
    
    """It eliminates duplicates from the list of the countries"""
    def obtainDistinctCountries(self, listCounties):
        distinctCountries = []
        times = 0
        for i in listCounties:
            if i not in distinctCountries:
                distinctCountries.append(i)
        return distinctCountries
    
    """This function will count the countries from the list"""
    def countCountries(self, country, listCounties):
        times = 0
        for i in listCounties:
            if country == i:
                times += 1
        return times
    
    """This function will print the name of the countries and its ocurrence"""
    def printCountriesCount(self, countriesCountList):
        for i in countriesCountList:
            print(i.country, i.count)

    """This function will count the ocurrences that the program read from the file events.txt"""
    def getOcurrencesCountry(self):
        search_name = "source.geolocation.cc"
        country_list = []
        try:
            with open(self.getFileEvents()) as attacks:
                for attack in attacks:
                    # We comprobate that there is a geolocation available in the line
                    if search_name in attack:
                        attributes = attack.split(", ")
                        i = 0
                        while i < len(attributes):
                            g = attributes[i].split(": ")
                            #We are looking for the attribute "source.location.cc in each line:
                            for a in g:
                                if "\"source.geolocation.cc\""  == a:
                                    """We obtain the code of the country: """
                                    temp = len(g[1])
                                    s1 = g[1][:temp - 1]
                                    s2 = s1[1:]
                                    """print(s2)"""
                                    country_list.append(s2)
                            i += 1

            distinct_countries = self.obtainDistinctCountries(country_list)
            
            #We insert the countries and its ocurrence in the class 'Struct'
            for c in distinct_countries:
                countries.append(Country(c, self.countCountries(c, country_list)))

        except Exception:
            print("Error: File not found.")

    """This function makes a data frame with points to show on the map"""
    def loadData(self):
        data = pd.DataFrame({
            'name':nameCountries,
            'nº attacks':values,
            'lat':latitude,
            'lon':longitude
        })
        data
        return data

    """It generates the map itself with the bubblets around it"""
    def createMap(self):
        # Sort the dataframe’s rows by reports, in descending order:
        data = self.loadData().sort_values(by='nº attacks', ascending=0)

        #In the file output we can see the country, the ocurrences and the values of latitude and longitude
        file = open(FILEOUTPUT,"w")
        file.write(str(data))

        print("Loading the map...")
        
        # It does an empty map
        m = folium.Map(location=[0, 0], tiles="Mapbox Bright", zoom_start=2)

        # We will add markers on the map
        for i in range(0, len(data)):
            folium.Circle(
                location=[data.iloc[i]['lon'], data.iloc[i]['lat']],
                popup=data.iloc[i]['name'],
                radius=data.iloc[i]['nº attacks'] * 50.5,
                color='crimson',
                fill=True,
                fill_color='crimson'
            ).add_to(m)

        # Save it as html
        m.save('mymap.html')

    """It obtains the longitude and latitude using the file iso3166-1-alpha-2.txt"""
    def obtainLongitudeLatitude(self):
        try:
            with open(self.getFileCodeISOCountries()) as lines:
                for line in lines:
                    attributes = line.split(",")
                    temp = len(attributes[0])
                    s1 = attributes[0][:temp - 1]
                    code = s1[1:]
                    lon = attributes[1]
                    lat = attributes[2]
                    temp_aux = len(attributes[3])
                    a = attributes[3][:temp_aux - 2]
                    name = a[1:]
                    
                    # We insert the data on the lists
                    i = 0
                    while i < len(countries):
                        if code == countries[i].country:
                            nameCountries.append(name)
                            values.append(int(countries[i].count))
                            longitude.append(float(lon))
                            latitude.append(float(lat))
                        i += 1

        except Exception:
            print("Error: File not found.")

s = Map("events.txt", "iso3166-1-alpha-2.txt")
s.getOcurrencesCountry()
s.obtainLongitudeLatitude()
s.createMap()

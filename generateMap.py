"""
    Author: "Javier Gombao"
    File: generateMap.py

    The purpose of this script is to obtain all the names of the countries which IntelMQ has detected as a cyber threat

"""

countriesCount = []
nameCountries =[]
value = []
latitude = []
longitude = []


class Struct():
    def __init__(self, country, count):
        self.country = country
        self.count = count

class generateMap(object):

    def __init__(self, fileEvents, fileCodeISOCountries):
        self._fileEvents=fileEvents
        self._fileCodeISOCountries=fileCodeISOCountries

    def getFileEvents(self):
        """Returns the fileInput."""
        return self._fileEvents

    def getFileCodeISOCountries(self):
        """Returns the fileInput."""
        return self._fileCodeISOCountries

    def obtainDistinctCountries(self, listCounties):
        distinctCountries = []
        times = 0
        for i in listCounties:
            if i not in distinctCountries:
                distinctCountries.append(i)
        return distinctCountries


    def countCountries(self, country, listCounties):
        times = 0
        for i in listCounties:
            if country == i:
                times += 1
        return times

    def printCountriesCount(self, countriesCountList):
        for i in countriesCountList:
            print(i.country, i.count)

    def printItemsMap(self, itemsMapList):
        for i in itemsMap:
            print(i.country, i.count)

    def getOcurrencesCountry(self):
        search_name = "source.geolocation.cc"
        country_list = []
        try:
            with open(self.getFileEvents()) as attacks:
                for attack in attacks:
                    """we comprobate that there is a geolocation available in the line"""
                    if search_name in attack:
                        attributes = attack.split(", ")
                        i = 0
                        while i < len(attributes):
                            g = attributes[i].split(": ")
                            """We are looking for the attribute "source.location in each line: """
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

            for c in distinct_countries:
                countriesCount.append(Struct(c, self.countCountries(c, country_list)))


        except Exception:
            print("Error: File not found.")


    def obtainLongitudeLatitude(self):

        try:
            with open(self.getFileCodeISOCountries()) as lines:
                for line in lines:
                    attributes = line.split(",")
                    temp = len(attributes[0])
                    s1 = attributes[0][:temp - 1]
                    code = s1[1:]
                    lat = attributes[1]
                    lon = attributes[2]
                    temp_aux = len(attributes[3])
                    a = attributes[3][:temp_aux - 2]
                    name = a[1:]

                    i = 0
                    while i < len(countriesCount):
                        if code == countriesCount[i].country:
                            nameCountries.append(name)
                            value.append(countriesCount[i].count)
                            latitude.append(lat)
                            longitude.append(lon)

                        i += 1


        except Exception:
            print("Error: File not found.")

s = generateMap("events.txt", "iso3166-1-alpha-2.txt")
s.getOcurrencesCountry()
s.obtainLongitudeLatitude()

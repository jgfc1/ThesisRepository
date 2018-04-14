"""
    Author: "Javier Gombao"
    File: generateMap.py

    The purpose of this script is to obtain all the names of the countries which IntelMQ has detected as a cyber threat

"""

class Struct():
    def __init__(self, country, count):
        self.country = country
        self.count = count

class generateMap(object):

    def __init__(self, fileInput):
        self._fileInput=fileInput

    def getFileInput(self):
        """Returns the fileInput."""
        return self._fileInput

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

    def getOcurrencesCountry(self):
        search_name = "source.geolocation.cc"
        country_list = []
        try:
            with open(self.getFileInput()) as attacks:
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

            countriesCount = []
            for c in distinct_countries:
                countriesCount.append(Struct(c, self.countCountries(c, country_list)))

            self.printCountriesCount(countriesCount)


        except Exception:
            print("Error: File not found.")


"""
    def readFile(self):
        search_name = "source.geolocation.cc"
        try:
            with open(self.getFileInput()) as attacks:
                for attack in attacks:
                    if search_name in attack:
                        attributes = attack.split(", ")
                        i = 0
                        while i < len(attributes):
                            g = attributes[i].split(": ")
                            for a in g:
                                if "\"source.geolocation.cc\""  == a:
                                    temp = len(g[1])
                                    s1 = g[1][:temp - 1]
                                    s2 = s1[1:]
                                    print(s2)

                            i += 1
        except Exception:
            print("Error: File not found.")
"""

s = generateMap("events.txt")
s.getOcurrencesCountry()


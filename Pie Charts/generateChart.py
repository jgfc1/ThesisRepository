"""
    Author: "Javier Gombao Fernandez-Calvillo"
    eMail: a00248414@student.ait.ie
    College: Athlone Institute of Technology (AIT)
    Subject: Final Project
    File: generateMap.py

    The purpose of this code is to obtain graphics in order to represents the data of IntelMQ:
    nameCountries: it provides the name if the country. Examples: Ireland, Spain, England, France...
    values: it defines the number of times which the country apperars in the result file given by IntelMQ
    latitude: it defines the latitude value
    longitude: it defines the longitude value
"""

# Import modules
import matplotlib.pyplot as plt
import pandas as pd

# Variables which we are going to use in the program
classificationTaxonomyCount = []
FILEOUTPUT = "output_classification_malware.txt"

# We configure the size of the table to show in the fileoutput
pd.set_option('display.max_row', 900)


class Struct():
    def __init__(self, taxonomy, count):
        self.taxonomy = taxonomy
        self.count = count

class generateChart(object):
    """Constructor of the function"""

    def __init__(self, fileEvents):
        self._fileEvents = fileEvents

    """It returns the name of the fileEvents"""

    def getFileEvents(self):
        return self._fileEvents

    """It eliminates duplicates from the list of the taxonomy"""
    def obtainDistinctTaxonomy(self, classificationTaxonomyList):
        distinctTaxonomy = []
        for i in classificationTaxonomyList:
            if i not in distinctTaxonomy:
                distinctTaxonomy.append(i)
        return distinctTaxonomy

    """This function will count the taxonomy from the list"""
    def countTaxonomy(self, taxonomy, classificationTaxonomyList):
        times = 0
        for i in classificationTaxonomyList:
            if taxonomy == i:
                times += 1
        return times

    """This function will print the name of the countries and its ocurrence"""
    def printTaxonomy(self, classificationTaxonomyList):
        for i in classificationTaxonomyList:
            print(i.taxonomy, i.count)

    """This function will count the ocurrences that the program read from the file events.txt"""

    def getOcurrences(self, search_name):
        taxonomy_list = []
        try:
            with open(self.getFileEvents()) as attacks:
                for attack in attacks:
                    # We comprobate that there is a taxonomy available in the line
                    if search_name in attack:
                        attributes = attack.split(", ")
                        i = 0
                        while i < len(attributes):
                            g = attributes[i].split(": ")
                            # We are looking for the attribute "source.location.cc in each line:
                            for a in g:
                                if "\""+search_name+"\"" == a:
                                    """We obtain the code of the country: """
                                    temp = len(g[1])
                                    s1 = g[1][:temp - 1]
                                    s2 = s1[1:]
                                    if "malicious code" in s2:
                                        taxonomy_list.append("malicious code")
                                    elif "fraud" in s2:
                                        taxonomy_list.append("fraud")
                                    elif "abusive content" in s2:
                                        taxonomy_list.append("abusive content")
                                    else:
                                        taxonomy_list.append(s2)
                            i += 1
            distinct_taxonomy = self.obtainDistinctTaxonomy(taxonomy_list)
            # We insert the countries and its ocurrence in the class 'Struct'

            for c in distinct_taxonomy:
                classificationTaxonomyCount.append(Struct(c, self.countTaxonomy(c, taxonomy_list)))

            if not classificationTaxonomyCount:
                print("No search matches")
            else:
                file = open(FILEOUTPUT, "w")
                data = self.loadData().sort_values(by='Count', ascending=0)
                print(str(data))
                file.write(str(data))

        except Exception:
            print("Error: File not found.")

    def loadData(self):
        taxonomy = []
        count = []
        for i in classificationTaxonomyCount:
            taxonomy.append(i.taxonomy)
            count.append(i.count)
        data = pd.DataFrame({
            'Taxonomy': taxonomy,
            'Count': count
        })
        return data

    """It generates the graph itself with the bubblets around it"""
    def createChart(self):
        if classificationTaxonomyCount:
            x = []
            labels = []
            for i in classificationTaxonomyCount:
                x.append(i.count)
                labels.append(i.taxonomy)
            plt.pie(x, labels=labels, autopct='%1.1f%%')
            plt.axis('equal')
            plt.show()

s = generateChart("events.txt")
s.getOcurrences("event_description.text")
s.createChart()

# Thesis Repository: An Analysis of Correlations of Cyber Attacks from several Threat Resources
This is the repository where you can find all the code related with my thesis in Athlone Institute of Technology (AIT). We have based our studies in the following botnet:

![alt text](http://1.bp.blogspot.com/-Vauukd4x9Jo/WtPa7Ma7NQI/AAAAAAAABpo/vcOmE_VbcYsXnjBk6VJeDmZirdVOF1odACK4BGAYYCw/s1600/Botnet.jpeg)

## Collector Bot: red nodes
It retrieves data from internal or external sources, the results are reports that consist of many individual data sets / log lines.

## Parser bot: green nodes
It takes the data sets and log lines which the collector bots has processes and it gives them a defined structure.

## Expert bot: blue nodes
It adds more content to the existing events such as geographic location information (country code), abuse contacts, type of the attaks...

## Output bot: yellow nodes
It writes the events to databases, REST-APIs, files or any other data sink.
The graph generate a file output which contains the resources which the program has correlated in a text format. The following line is an example of one line of this file:

### Format of the file-output: 
{"feed.accuracy": 100.0, "feed.name": "Abuse.ch Zeus Bad Domains", "feed.provider": "Abuse.ch", "feed.url": "https://zeustracker.abuse.ch/blocklist.php?download=baddomains", "time.observation": "2018-04-15T16:37:27+00:00", "classification.taxonomy": "malicious code", "classification.type": "c&c", "source.fqdn": "afobal.cl", "raw": "YWZvYmFsLmNs", "malware.name": "zeus", "source.ip": "66.7.198.165", "source.asn": 33182, "source.network": "66.7.192.0/19", "source.geolocation.cc": "US", "source.registry": "ARIN", "source.allocated": "2006-05-18T00:00:00+00:00", "source.as_name": "DIMENOC - HostDime.com, Inc., US"}

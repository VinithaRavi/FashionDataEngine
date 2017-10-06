from google import search
import urllib
import urllib.request
import json
from bs4 import BeautifulSoup

def google_scrape(url):
    #s = url.read
    thepage =  urllib.request.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

with open('brands.json') as data_file:
    data = json.load(data_file)

for i in data:
    brand_name=i['brand']
    website=list(search(brand_name, stop=1))[0]
    i['website']=website
    print(brand_name,website)

with open('brands.json', "w") as jsonFile:
  json.dump(data, jsonFile)
# for i in data:
#   print (i)
#     f:
#
#       #a = google_scrape(url)
# i = 1
# query = 'A.L.C'
# print(list(search(query, stop=1))[0])
#    #  a = google_scrape(url)
#    #  print (str(i) + ". " + a)
#    #  print (url)
#    # # print (" ")
#    # i += 1
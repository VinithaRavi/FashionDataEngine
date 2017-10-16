from pymongo import MongoClient
from bson import ObjectId
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

with open('designers.json') as data_file:
    data = json.load(data_file)

client = MongoClient()
db= client.FashionData
Designer=db['Designer']
print(db)



for i in data:
    try:
        designer_name=i['designer']
        website=list(search(designer_name, stop=1))[0]
        i['website']=website
        db.Designer.insert({'name':designer_name, 'website': website})
        print(designer_name, website)
    except:
        print(designer_name)


    #break


#with open('designers.json', "w") as jsonFile:
#  json.dump(data, jsonFile)

cursor = Designer.find()
for document in cursor:
    print(document)
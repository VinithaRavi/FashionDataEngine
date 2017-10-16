from pymongo import MongoClient
from bson import ObjectId
import json
client = MongoClient()
print(client)
db= client.test
brand=db['Brand']
print(db)


# with open('../brands.json') as data_file:
#     data = json.load(data_file)
#     for br in data:
#         db.Brand.insert({ 'name': br['brand'], 'website': br['website']});
# cursor = brand.find()
#
# db.Brand.remove({"_id": ObjectId('59e3fdffea90c90405c88ca1')})
# for document in cursor:
#     print(document)
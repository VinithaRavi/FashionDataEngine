from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
#from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)

print("Success")
@app.route('/designers', methods=['GET'])
def get_all_brands():
  designer = mongo.db.Designer
  output = []
  for s in designer.find():
    output.append({'name' : s['name'], 'website' : s['website']})
  return jsonify({'result' : output})

@app.route('/designers/<name>', methods=['GET'])
def get_one_brand(name):
  designer = mongo.db.Designer
  s = designer.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'website' : s['website']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/designers', methods=['POST'])
def add_brand():
  designer = mongo.db.Designer
  name = request.json['name']
  website = request.json['website']
  brand_id = designer.insert({'name': name, 'website': website})
  new_brand = designer.find_one({'_id': brand_id })
  output = {'name' : new_brand['name'], 'website' : new_brand['website']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
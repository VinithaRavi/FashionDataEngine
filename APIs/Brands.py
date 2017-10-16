from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson import json_util
from flask import Response
#from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)

print("Success")
@app.route('/brands', methods=['GET'])
def get_all_brands():
  brand = mongo.db.Brand
  output = []
  for s in brand.find():
    output.append({'name' : s['name'], 'website' : s['website']})
  return jsonify({'result' : output})

@app.route('/brands/<name>', methods=['GET'])
def get_one_brand(name):
  brand = mongo.db.Brand
  s = brand.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'website' : s['website']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/brands', methods=['POST'])
def add_brand():
  brand = mongo.db.Brand
  name = request.json['name']
  website = request.json['website']
  brand_id = brand.insert({'name': name, 'website': website})
  new_brand = brand.find_one({'_id': brand_id })
  output = {'name' : new_brand['name'], 'website' : new_brand['website']}
  return jsonify({'result' : output})


@app.route('/designers', methods=['GET'])
def get_all_designers():
  designer = mongo.db.Designer
  output = []
  for s in designer.find():
    output.append({'name' : s['name'], 'website' : s['website']})
  return jsonify({'result' : output})

@app.route('/designers/<name>', methods=['GET'])
def get_one_designer(name):
  designer = mongo.db.Designer
  s = designer.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'website' : s['website']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/designers', methods=['POST'])
def add_designer():
  designer = mongo.db.Designer
  name = request.json['name']
  website = request.json['website']
  brand_id = designer.insert({'name': name, 'website': website})
  new_brand = designer.find_one({'_id': brand_id })
  output = {'name' : new_brand['name'], 'website' : new_brand['website']}
  return jsonify({'result' : output})


@app.route('/products', methods=['GET'])
def get_all_product():
  product = mongo.db.Product
  output = []
  for s in product.find():
    output.append({'name' : s['name'],
                   'link' : s['link'],
                   'code': s['code'],
                   'color': s['color'],
                   'description': s['description'],
                   'designers': s['designers'],
                   'usd_price': s['usd_price'],
                   'gender': s['gender'],
                   'image_urls': s['image_urls'],
                   'raw_color': s['raw_color'],
                   'sale_discount': s['sale_discount'],
                   'stock_status': s['stock_status'],
                   'subtype': s['subtype'],
                   'type': s['type'],
                   })
  return Response(
    json_util.dumps({'result' : output}),
    mimetype='application/json'
)


@app.route('/products/<name>', methods=['GET'])
def get_one_product(name):
  product = mongo.db.Product
  s = product.find_one({'name' : name})
  if s:
    output = {'name' : s['name'],
                   'link' : s['link'],
                   'code': s['code'],
                   'color': s['color'],
                   'description': s['description'],
                   'designers': s['designers'],
                   'usd_price': s['usd_price'],
                   'gender': s['gender'],
                   'image_urls': s['image_urls'],
                   'raw_color': s['raw_color'],
                   'sale_discount': s['sale_discount'],
                   'stock_status': s['stock_status'],
                   'subtype': s['subtype'],
                   'type': s['type'],
                   }
  else:
    output = "No such name"
  return Response(
    json_util.dumps({'result': output}),
    mimetype='application/json'
  )
@app.route('/products', methods=['POST'])
def add_product():
  designer = mongo.db.Product
  name = request.json['name']
  website = request.json['website']
  brand_id = designer.insert({'name': name, 'website': website})
  new_brand = designer.find_one({'_id': brand_id })
  output = {'name' : new_brand['name'], 'website' : new_brand['website']}
  return jsonify({'result' : output})
if __name__ == '__main__':
    app.run(debug=True)
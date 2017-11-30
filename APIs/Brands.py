from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson import json_util
from flask import Response
from urllib.parse import urlparse
#from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

@app.errorhandler(404)
def everything(e):
    return app.send_static_file('index.html')
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


@app.route('/product_length', methods=['GET'])
def product_length():
    product = mongo.db.Product
    prod_length = product.count()
    return Response(
        json_util.dumps({'length': prod_length}),
        mimetype='application/json')

@app.route('/products', methods=['GET'])
def get_all_product():
  query_string = request.query_string
  index=request.args.get('index')
  #index = query_string.split('=')
  #print(o)
  product = mongo.db.Product
  output = []
  db_result=product.find().limit(5).skip(int(index))
  #print(db_result.count(True))
  if db_result.count(True)>0:
    for s in db_result:
    #print(s)
        output.append({'id': str(s['_id']),
                    'name' : s['name'] if 'name' in s else "",
                   'url' : s['url'] if 'url' in s else "",
                   #'code': s['code'],
                   'color': s['color'] if 'color' in s else "",
                   'description': s['description'] if 'description' in s else "",
                   'designer': s['designer'] if 'designer' in s else "",
                   #'usd_price': s['usd_price'],
                   #'gender': s['gender'],
                   'image_urls': s['image_urls'] if 'image_urls' in s else "",
                   'details':s['details'] if 'details' in s else "",
                   'price':s['price'] if 'price' in s else ""
                   #'raw_color': s['raw_color'],
                   #'sale_discount': s['sale_discount'],
                   #'stock_status': s['stock_status'],
                   #'subtype': s['subtype'],
                   #'type': s['type'],
                   })
    return Response(
    json_util.dumps({'result' : output, 'hasMore':'true' }),
    mimetype='application/json')
  else:
      return Response(
          json_util.dumps({'result': [], 'hasMore': 'false'}),
          mimetype='application/json')

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
    app.run(host='0.0.0.0')
    app.run(debug=True)
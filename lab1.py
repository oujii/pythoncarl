from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql11428814:SJpvCk73tN@sql11.freemysqlhosting.net/sql11428814'
db = SQLAlchemy(app)



class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))
    price = db.Column(db.String(120))
    category = db.Column(db.String(120))
    vendor = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description} - {self.price} - {self.category} - {self.vendor}"


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.first_name} - {self.last_name} - {self.email} - {self.id}"
        






@app.route('/')

def index():
    return 'hello!'



########### CUSTOMERS ##############


@app.route('/customers')

def get_customers():

    customers = Customers.query.all()

    output = []
    for customer in customers:
        customer_data = {'first_name': customer.first_name, 'last_name': customer.last_name, 'email': customer.email}
        output.append(customer_data)

    return {'customers': output}



@app.route('/customers/<id>')
def get_customer(id):
    customer = Customers.query.get_or_404(id)
    return {'first_name': customer.first_name, 'last_name': customer.last_name, 'email': customer.email}


@app.route('/customers', methods=['POST'])
def add_customer():
    customer = Customers(first_name=request.json['first_name'], last_name=request.json['last_name'], email=request.json['email'])
    db.session.add(customer)
    db.session.commit()
    return {'id': customer.id}


@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customers.query.get(id)
    if customer is None:
        return {'error': 'not found'}
    db.session.delete(customer)
    db.session.commit()
    return {'message': 'yeet'}



############# PRODUCTS #####################


@app.route('/products')

def get_products():

    products = Products.query.all()

    output = []
    for product in products:
        product_data = {'name': product.name, 'description': product.description, 'price': product.price, 'category': product.category, 'vendor': product.vendor}
        output.append(product_data)

    return {'products': output}



@app.route('/products/<id>')
def get_product(id):
    product = Products.query.get_or_404(id)
    return {'name': product.name, 'description': product.description, 'price': product.price, 'category': product.category, 'vendor': product.vendor}


@app.route('/products', methods=['POST'])
def add_product():
    product = Products(name=request.json['name'], description=request.json['description'], price=request.json['price'], category=request.json['category'], vendor=request.json['vendor'])
    db.session.add(product)
    db.session.commit()
    return {'id': product.id}


@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Products.query.get(id)
    if product is None:
        return {'error': 'not found'}
    db.session.delete(product)
    db.session.commit()
    return {'message': 'yeet'}

from flask import Flask, render_template
from lib.product import Product
import os

DATA_DIRECTORY = os.path.join("static", "data")

app = Flask(__name__)

@app.route('/')
def index():
    data_directories = os.listdir(DATA_DIRECTORY)

    products = list()
    for directory in data_directories:
        product_path = os.path.join(DATA_DIRECTORY, directory)
        
        if os.path.isdir(product_path):
            products.append(Product(product_path))
    
    return render_template('index.html',
                products=products)
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_NAME = "ecommerce.db"

@app.route('/api/products', methods = ['GET'])
def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()

    products = [dict(row) for row in rows]
    return jsonify(products), 200

@app.route('/api/products/<string:product_id>', methods = ['GET'])
def get_product_by_id(product_id):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?",(product_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify(dict(row)),200
    else:
        return jsonify({"error" : "product not found"}), 404
    
if __name__ =='__main__':
    app.run(debug=True)
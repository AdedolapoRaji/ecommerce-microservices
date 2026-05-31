from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({
        "service": "Product Catalog",
        "status": "Healthy",
        "products": [
            {"id": 1, "name": "Laptop", "price": 999.99},
            {"id": 2, "name": "Wireless Mouse", "price": 25.50}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

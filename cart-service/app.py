from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify({
        "service": "Shopping Cart",
        "status": "Healthy",
        "cart_items": [{"product_id": 1, "quantity": 1}],
        "total_items": 1
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

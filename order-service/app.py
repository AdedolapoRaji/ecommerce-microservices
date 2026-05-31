from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({
        "service": "Order Processing",
        "status": "Healthy",
        "order_id": "ORD-2026-X",
        "payment": "Verified"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

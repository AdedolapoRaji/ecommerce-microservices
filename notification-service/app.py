from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['GET'])
def get_notifications():
    return jsonify({
        "service": "Notification Engine",
        "status": "Healthy",
        "dispatch_type": "Email"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

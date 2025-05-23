from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # لتفادي مشاكل CORS مع React

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from Flask Backend!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

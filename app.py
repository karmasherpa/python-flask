from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this demo Python app.'

@app.route('/api/data')
def get_data():
    data = {
        'title': 'Hello from Flask',
        'message': 'This data is served from Flask to your Angular app!'
    }
    return jsonify(data)

CORS(app)

if __name__ == '__main__':
    # Change the host and port here
    app.run(host='0.0.0.0', port=5001, debug=True)

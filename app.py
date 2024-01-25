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
    app.run(debug=True)

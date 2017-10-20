from flask import Flask, jsonify
from apis.v1.views import api
app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api/v1")

@app.route('/')
def mainpage():
    return jsonify({'message': 'Hello from Main'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5440)
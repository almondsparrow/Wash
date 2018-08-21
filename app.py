from flask import Flask, jsonify, request
from chotautils import getID
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome!"

@app.route('/search', methods=['POST'])
def returnID():
    mode = request.form.get('mode')
    data = request.form.get('data')
    details = getID(mode, data)
    status=404
    if details:
        status=200
    return jsonify({"status": status, "details": details})

if __name__ == '__main__':
    app.run(debug=True)
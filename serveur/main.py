from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/data')
def data():
    jsonfile = open("data.json")
    content = jsonfile.read()
    return jsonify(content)

if __name__ == "__main__":
    app.run(debug=True)
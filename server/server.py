from flask import Flask,send_file,abort,redirect
from flask_cors import CORS, cross_origin
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir) 

def jsonToDict(json_file):
    with open(json_file,encoding="utf-8") as f:
        data = json.load(f)
    return data

countries = jsonToDict("data.json")

def search(entry):
    for country in countries:
       for value in [country["name"],country["alpha2Code"],country["alpha3Code"],country["numericCode"]]:
           if entry.upper() == value.upper(): return country
    abort(404)
       
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS']='Content-Type'

@app.route('/api/v1/country/<entry>')
@cross_origin()
def getCountry(entry):
    return search(entry)

@app.route('/api/v1/country/flag/<entry>')
@cross_origin()
def getFlag(entry):
    requested = search(entry)
    return send_file(f"./flags/{requested['alpha2Code']}.png", mimetype='image/png')

@app.route('/')
@app.route('/<anymatch>')
@app.route('/<anymatch>/<path:rest>')
@cross_origin()
def route(anymatch=None,rest=None):
    return redirect("/api/v1/country/TN")

if __name__ == '__main__': app.run(port=5000)
from flask import Flask,send_file,abort,redirect
from flask_cors import CORS, cross_origin
import json

def jsonToDict(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

config = jsonToDict("config.json")
data_path = config["dataPath"]

def search(entry):
    countries = jsonToDict(f"{data_path}all.json")
    
    #Scan Levels
    first_scan = None
    intermidiate_scan = None
    deep_scan = None
    
    for country in countries:
       for value in [country["name"],country["alpha-2"],country["alpha-3"],country["country-code"]]:
           if entry.upper() == value.upper(): first_scan = country
    
    if config["scanLevel"] >= 1:
        if first_scan==None:
            for country in countries:
                for value in country.values():
                    if entry.upper() == value.upper(): 
                        intermidiate_scan = country
                        break
                    if entry.upper() in value.upper(): 
                        deep_scan = country
                        break
                
    return first_scan if first_scan is not None else intermidiate_scan if intermidiate_scan is not None else deep_scan if deep_scan is not None else abort(404)
       

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
    return send_file(f"{data_path}flags/{requested['alpha-2']}.png", mimetype='image/png')

@app.route('/')
@app.route('/<anymatch>')
@app.route('/<anymatch>/<path:rest>')
@cross_origin()
def route(anymatch=None,rest=None):
    return redirect("/api/v1/country/TN")


if __name__ == '__main__': app.run(port=int(config['port']))
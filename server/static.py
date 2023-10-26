import json
import os

def navigate():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir) 

def jsonToDict(json_file):
    with open(json_file,encoding="utf-8") as f:
        data = json.load(f)
    return data

def dictToJson(json_file,dictionary):
    with open(json_file,"w",encoding="utf-8") as f:
        json.dump(dictionary, f)
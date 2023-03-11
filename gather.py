from os import path
import requests
import shutil 
import time
import html
import json

def jsonToDict(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

flagpath = "./data/flags/"

def download_image(url,file_name):
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

def get_all_flags():
    items = jsonToDict("./data/all.json")
    for item in items:
        if not path.exists(flagpath+item["alpha-2"]+".png"):
            download_image("https://countryflagsapi.com/png/"+html.escape(item["alpha-2"].replace(" ","%20")),flagpath + item["alpha-2"]+".png")
            time.sleep(0.5)
        
get_all_flags()
from os import path
import requests
import shutil 
import time
import html
import json
import sys

def jsonToDict(json_file):
    with open(json_file,encoding="utf-8") as f:
        data = json.load(f)
    return data

def dictToJson(json_file,dictionary):
    with open(json_file,'w',encoding="utf-8") as f:
        json.dump(dictionary, f,ensure_ascii=False) 
            

def download_image(url,file_name):
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

def get_all_flags(update=None):
    items = jsonToDict("./data/all.json")
    for item in items:
        if not path.exists("./data/flags/"+item["alpha-2"]+".png") or update:
            download_image("https://countryflagsapi.com/png/"+html.escape(item["alpha-2"].replace(" ","%20")),"./data/flags/" + item["alpha-2"]+".png")
            time.sleep(0.5)

def seperate():
    town = jsonToDict("./data/cities.json")
    for key in town.keys():
        prev = {key : town[key]}
        if path.exists(f"./data/cities/{key[0]}.json"):
            prev = jsonToDict(f"./data/cities/{key[0]}.json")
            prev[key] = town[key]
        dictToJson(f"./data/cities/{key[0]}.json", prev)
        
#seperate()
#get_all_flags(sys.argv[1])
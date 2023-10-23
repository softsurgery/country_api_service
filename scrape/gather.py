from os import path
import shutil 
import time
import html
import json
import sys
import requests

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
            download_image("https://countryflagsapi.com/png/"+item["alpha-2"],"./data/flags/" + item["alpha-2"]+".png")
            time.sleep(0.5)

def migrate_ph1():
    items = jsonToDict("./data/ISO-3166-Countries-with-Regional-Codes.json")
    newItems = [
        {
            "name": item["name"],
            "alpha-2": item["alpha-2"],
            "alpha-3": item["alpha-3"],
            "country-code": item["country-code"],
        } for item in items
    ]
    dictToJson("./data/ISO-3166-Countries-with-Regional-Codes.json", newItems)



url = f'https://restcountries.com/v2/alpha/'


def jsonToDict(json_file):
    with open(json_file,encoding="utf-8") as f:
        data = json.load(f)
    return data

def dictToJson(json_file,dictionary):
    with open(json_file,'w',encoding="utf-8") as f:
        json.dump(dictionary, f,ensure_ascii=False) 
        
def load_infotmations():        
    country_codes = [code["alpha-2"] for code in jsonToDict("./data/ISO-3166-Countries-with-Regional-Codes.json")]
    file_content = []
    for code in country_codes:
        try:
            country = json.loads(requests.get(url+code).text)
            del country["flags"]
            del country["flag"]
            file_content.append(country)
            print(f"Successfully imported information for '{code}'")
        except:
            print(f"An error occurred while importing information for '{code}'")
    dictToJson("./data/country.json",file_content)

load_infotmations()
#migrate_ph1()
#get_all_flags(sys.argv[1])
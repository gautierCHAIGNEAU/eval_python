import requests
import json

def getDonnees():
    r = requests.get("http://localhost:5000/data")
    myjson = json.loads(r.text)
    return myjson

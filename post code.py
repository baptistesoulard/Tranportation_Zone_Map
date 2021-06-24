import json
import urllib
import requests

url = 'https://parseapi.back4app.com/classes/CH?limit=10000&keys=adminCode1,adminName3,placeName,postalCode'
headers = {
    'X-Parse-Application-Id': 'zS2XAEVEZAkD081UmEECFq22mAjIvX2IlTYaQfai', # This is the fake app's application id
    'X-Parse-Master-Key': 't6EjVCUOwutr1ruorlXNsH3Rz65g0jiVtbILtAYU' # This is the fake app's readonly master key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
print(json.dumps(data, indent=2))
import json
import readJson

data = {}

data['settings'] = []
data['settings'].append({
    'power': '1',
    'light': '1',
    'increaseTemp': '0',
    'decreaseTemp': '0',
    'increaseTime': '0',
    'decreaseTime': '0',
    'temperature': '120'
    })

with open('data.json', 'w') as outfile:
    json.dump(data,outfile)
    
readJson.parseJson('data.json')
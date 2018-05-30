import json


def parseJson(file):
    with open(file) as json_file:
        data = json.load(json_file)
        for s  in data['settings']:
            print('Power On/Off: ' + s['power'])
            print('Light On/Off: ' + s['light'])
            print('Temperature Up: ' + s['increaseTemp'])
            print('Temperate Down: ' + s['decreaseTemp'])
            print('Time Up: ' + s['increaseTime'])
            print('Time Down: ' + s['decreaseTime'])
            print('Temperature Set At: ' + s['temperature'])
    return s
        
    
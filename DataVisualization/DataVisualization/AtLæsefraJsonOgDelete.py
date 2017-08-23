import json
import requests

response = requests.get('http://apps.odense.dk/data/newtags/115-dk-full.json')
data = response.json()

for x in data['features']:
    for y in x['tags']:
        try:
            if not y['primary']:
                del y['primary']
        except:
            print("This key doesn't have the value")
    for y in x['properties']:
        try:
            count = 0
            for z in range(0,len(x['properties'][y]['value'])):
                if not x['properties'][y]['value'][count]['value']:
                    del x['properties'][y]['value'][count]
                else:
                    count += 1
        except:
            print("This key doesn't have the value")
        try:
            if str(x['properties'][y]['value']) == '[]':
                del x['properties'][y]['value']
        except:
            print("This key doesn't have the value")

with open('data2.json', 'w') as outfile:
    json.dump(data, outfile)

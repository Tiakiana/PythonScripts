import pandas as pd
import requests
import sys
from pymongo import MongoClient
from bson import ObjectId
client = MongoClient()
db = client.Trafik_DB
data = db.Measurements


# for fixing ObjectId when finding item in database
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



'''
Argv indeholder alle de ting som vi f�r fra kalderen af scriptet
argv[0] er navnet p� dette script
argv[0+n] er n argument

'''




parameters = {"from": str(pd.to_datetime(str(sys.argv[1]+" "+sys.argv[2]))), "to": str(pd.to_datetime(str(sys.argv[3]+" "+sys.argv[4])))}
response = requests.get("http://adm-trafik-01.odknet.dk:1000/api/reader/GetMeasurementsBetweenDates?from=2017-07-08%2000:00:00&to=2017-07-10%2000:00:00&stationName=Rismarksvej")
data = pd.read_json(response.content)
#print(data.groupby(data.carType).speed.mean())
print(data.speed.mean())
data['dateTime'] = pd.to_datetime(data.dateTime)
print(data)
def GetData(carType = None, lane = None, stationname = None):
    res = data
    if carType is not None:
        res = res[res.carType == carType]
    if lane is not None:
        res = res[res.lane == lane]
    if stationname is not None:
        res = res[res.stationName == stationname]
    return res

def GetAverageSpeed(dataset):
    if len(dataset)>0:
        counter = 0
        for item in dataset.speed:
            counter = counter + item
        return (counter/ len(dataset))
    else:
        return 0

print((GetAverageSpeed(GetData(2,2,"Rismarksvej km 4,203"))))
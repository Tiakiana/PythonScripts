import pandas as pd
import requests
import sys

'''
Argv indeholder alle de ting som vi får fra kalderen af scriptet
argv[0] er navnet på dette script
argv[0+n] er n argument

'''

fromhere = '2017-07-18 18:50:12'
tohere = '2017-07-20 19:50:12'
parameters = {"from": str(pd.to_datetime(fromhere)), "to": str(pd.to_datetime(tohere))}
#parameters = {"from": str(pd.to_datetime(str(sys.argv[1]+" "+sys.argv[2]))), "to": str(pd.to_datetime(str(sys.argv[3]+" "+sys.argv[4])))}
response = requests.get("http://adm-trafik-01.odknet.dk:1000/api/reader/GetMeasurementsBetweenDates", params=parameters)
data = pd.read_json(response.content)
#print(data.head)

data['dateTime'] = pd.to_datetime(data.dateTime)

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


print(GetData(2,1,'Rismarksvej km 4,203').head())
#print(GetAverageSpeed(GetData(int(sys.argv[5][1]),int(sys.argv[6][1]),str(sys.argv[7]))))
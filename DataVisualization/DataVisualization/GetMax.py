import pandas as pd
import requests
import sys



'''
Argv indeholder alle de ting som vi får fra kalderen af scriptet
argv[0] er navnet på dette script
argv[0+n] er n argument

'''

parameters = {"from": "2017-07-18 00:00:00", "to": "2017-07-20 00:00:00"}
response = requests.get("http://adm-trafik-01.odknet.dk/api/Reader/GetMeasurementsBetweenDates", params=parameters)
print(response.status_code)
data = pd.read_json(response.content)


#data = pd.read_csv(argv[1])

data['dateTime'] = pd.to_datetime(data.dateTime)


def GetData(carType = None, lane = None):
    res = data
    if carType is not None:
        res = res[res.carType == carType]
    if lane is not None:
        res = res[res.lane == lane]
    return res


print(max(GetData(2,1).speed))










    



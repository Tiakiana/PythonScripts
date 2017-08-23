'''
import pandas as pd
import requests
import sys




Argv indeholder alle de ting som vi får fra kalderen af scriptet
argv[0] er navnet på dette script
argv[0+n] er n argument



data = pd.read_csv(argv[1])

data['dateTime'] = pd.to_datetime(data.dateTime)


def GetData(carType = None, lane = None):
    res = data
    if carType is not None:
        res = res[res.carType == carType]
    if lane is not None:
        res = res[res.lane == lane]
    return res

def GetData(carType = None, lane = None, hour1 = None, hour2 = None, day = None):
    res = data
    if carType is not None:
        res = res[res.carType == carType]
    if lane is not None:
        res = res[res.lane == lane]
    if hour1 is not None:
        res = res[res.dateTime.dt.hour>= hour1]
    if hour2 is not None:
        res = res[res.dateTime.dt.hour< hour2]
    if day is not None:
        res = res[res.dateTime.dt.weekday_name == day]
    return res

def HowManyMeasurements(dataset):
    return len(dataset)



     


print(HowManyMeasurements24()))
'''


import pandas as pd
import requests
import sys

import io


data = pd.read_csv(io.StringIO(sys.argv[1]))
print(data.dtype)
data['dateTime'] = pd.to_datetime(data.dateTime)


def GetData(carType = None, lane = None):
    res = data
    if carType is not None:
        res = res[res.carType == carType]
    if lane is not None:
        res = res[res.lane == lane]
    return res


def HowManyMeasurements(dataset):
    return len(dataset)


def HowManyMeasurements24(dataset):
    res = []
    for x in range(0,24):
        res.append(HowManyMeasurements(GetData(int(sys.argv[2][1]),int(sys.argv[3][1]),x,x+1,None,None)))
    return res


print(HowManyMeasurements24(GetData(sys.argv[2],sys.argv[3])))

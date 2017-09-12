import pandas as pd
import requests
import sys

import io

'''
data = pd.read_csv(io.StringIO(sys.argv[1]))
print(data.dtype)
data['dateTime'] = pd.to_datetime(data.dateTime)
'''

#data = pd.read_table('C:\\Users\\jaarn\\Desktop\\Falenmaj.txt')
data = pd.read_csv(io.StringIO(sys.argv[1]))
data['dateTime'] = pd.to_datetime(data.dateTime)

#print(data.head)
def GetAverageSpeed(dataset):
    if len(dataset)>0:
        counter = 0
        for item in dataset.speed:
            counter = counter + item
        return (counter/ len(dataset))
    else:
        return 0

def GetData(carType = None, lane = None):
    res = data
    if carType is not None:
        res = res[res.carType == carType]
    if lane is not None:
        res = res[res.lane == lane]
    return res

    
#Giver counten på den enkelte dag


DFList = [group[1] for group in GetData(sys.argv[2],sys.argv[3]).groupby(data.datetime.dt.dayofyear)]
averages = []
for x in DFList:
    averages.append(GetAverageSpeed(x))

print(averages)

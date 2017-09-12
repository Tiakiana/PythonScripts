import pandas as pd
import requests
import sys



'''
Argv indeholder alle de ting som vi får fra kalderen af scriptet
argv[0] er navnet på dette script
argv[0+n] er n argument

'''

data = pd.read_table('C:\\Users\\jaarn\\Desktop\\AnderupMaj.txt')
data.rename(columns = {'class' : 'carType'}, inplace = True)

data['datetime'] = pd.to_datetime(data.datetime)




def GetData(carType = None, lane = None):
    res = data
    if carType is not None:
        res = res[res.carType == carType]
    if lane is not None:
        res = res[res.lane == lane]
    return res


def HowManyMeasurements(dataset):
    return len(dataset)

for x in range(0,13):
    print(len(GetData(x,None)))














    


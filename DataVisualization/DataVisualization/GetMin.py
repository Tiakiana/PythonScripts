import pandas as pd
import requests
import sys



'''
Argv indeholder alle de ting som vi får fra kalderen af scriptet
argv[0] er navnet på dette script
argv[0+n] er n argument

'''

data = pd.read_csv(argv[1])


data['dateTime'] = pd.to_datetime(data.dateTime)


def GetData(carType = None, lane = None):
    res = data
    if carType is not None:
        res = res[res.carType == carType]
    if lane is not None:
        res = res[res.lane == lane]
    return res



print(min(GetData(argv[2],argv[3])))










    



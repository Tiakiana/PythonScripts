import pandas as pd
import requests
import sys
import matplotlib.pyplot as mpl
import io

'''
data = pd.read_csv(io.StringIO(sys.argv[1]))
print(data.dtype)
data['dateTime'] = pd.to_datetime(data.dateTime)
'''

data = pd.read_table('C:\\Users\\jaarn\\Desktop\\Falenmaj.txt')
#data = pd.read_csv(io.StringIO(sys.argv[1]))
data['datetime'] = pd.to_datetime(data.datetime)
data.rename(columns = {'class' : 'cartype'}, inplace = True)
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
#print(data.head)
print("Kapb")
#print(data.isnull().speed)
#print("uggabuggah ",data.speed.isnull().count)
newthuibg = data[ (data.cartype == 0) & (data.speed>=80)]

#print(len(newthuibg))

#print(data.groupby(data.cartype).speed.agg(["count","min","max","mean"]))

#print(data.isnull().sum())
#print(data.describe())

#print(data.groupby(data.datetime.dt.dayofyear).speed.mean());
#print(data.groupby(data.cartype).speed.mean())
#data.groupby(data.cartype).speed.mean().plot(kind = "bar")
#mpl.show()

#print("Things that are of cars")
#print(data.groupby(data.cartype).speed.min())
#print(data.groupby(data.cartype).speed.max())

#print(data.groupby(data.cartype).speed.agg(["count","min","max","mean"]))
#print("Here be the things I wants now")
#print(data.groupby(data.cartype).speed.count())
res = []

res2 = data.groupby(data.cartype).speed.count()
print(res2)
for x in res2:
    res.append(x)

print("Res is:", res)

'''
print(data.cartype.value_counts)
print(pd.crosstab(data.cartype, data.speed))


#data.groupby(data.cartype).speed.agg(["count","min","max","mean"]).plot(kind="bar")
#mpl.show()
'''




#DFList = [group[1] for group in GetData(sys.argv[2],sys.argv[3]).groupby(data.datetime.dt.dayofyear)]
#averages = []
#for x in DFList:
#    averages.append(GetAverageSpeed(x))

#print(averages)


import pandas as pd
import requests
import sys

print(args[0])

#Først henter vi den ønskede fil:

parameters = {"from": "2017-07-18 00:00:00", "to": "2017-07-20 00:00:00"}
response = requests.get("http://adm-trafik-01.odknet.dk/api/Reader/GetMeasurementsBetweenDates", params=parameters)
print(response.status_code)
data = pd.read_json(response.content)

print(data.head)   # pd.read_table('C:\\Users\\jaarn\\Desktop\\Falenmaj.txt')

#preprocessing af data:
#gør data giv kolonnen et andet navn en klasse:
#gør gør dateTime kolonnen til rent faktisk date time objekter:

#data.rename(columns = {'type' : 'carType'}, inplace = True)

data['dateTime'] = pd.to_datetime(data.dateTime)
print(data.dateTime)

def GetFile(filepath):
    data = pd.read_table(filepath)
    data.rename(columns = {'class' : 'carType'}, inplace = True)
    data['dateTime'] = pd.to_datetime(dataframe_all.dateTime)
    print("File Loaded and raring to go")


def GetDataByDayName(dayOfWeek):
    res = data.dateTime.dt.weekday_name == dayOfWeek
    newdata = data[res]
    return newdata


def GetDataByClass(carType):
    return data[data.carType == carType]

def GetAverageSpeed(dataset):
    if len(dataset)>0:
        counter = 0
        for item in dataset.speed:
            counter = counter + item
        return (counter/ len(dataset))
    else:
        return 0

def GetAverageSpeedInTimeInterval(time1, time2, dataset = None):
    if dataset is None:
        return GetAverageSpeed(data[(data.dateTime.dt.hour>time1) & (data.dateTime.dt.hour<time2)])
    else:
        return GetAverageSpeed(dataset[(dataset.dateTime.dt.hour>=time1) & (dataset.dateTime.dt.hour<time2)])

def HowManyMeasurements(dataset):
    return len(dataset)


"""
Each parameter can be left out.
carType:int is the class of car you want, lane:int, hour1:int (inclusive) defines the hour of the day from when you want the data, hour2:int (exclusive) is the max hour you want data from.
"""
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


def GetAllAverageSpeedInTimeInterval(time1, time2):
    print("Printing average speed btwn 2 time intervals and a certain carType", time1,"-" ,time2)
    print("class 1: ", GetAverageSpeedInTimeInterval(time1,time2,GetDataByClass(1)) )
    print("class 2: ", GetAverageSpeedInTimeInterval(time1,time2,GetDataByClass(2)) )
    print("class 3: ", GetAverageSpeedInTimeInterval(time1,time2,GetDataByClass(3)) )
    print("class 4: ", GetAverageSpeedInTimeInterval(time1,time2,GetDataByClass(4)) )
    print("class 5: ", GetAverageSpeedInTimeInterval(time1,time2,GetDataByClass(5)) )
    print("class 6: ", GetAverageSpeedInTimeInterval(time1,time2, GetDataByClass(6)) )
    print("class 7: ", GetAverageSpeedInTimeInterval(time1,time2, GetDataByClass(7)) )
    print("class 8: ", GetAverageSpeedInTimeInterval(time1,time2, GetDataByClass(8)) )
    print("class 9: ", GetAverageSpeedInTimeInterval(time1,time2, GetDataByClass(9)) )






#print(GetData(1,1,1,3,None).head)
#print(GetData(1,None,None,14,None))
print("Antal målinger på en given dag pr time")
MeasureMonday = []
MeasureSunday = []
for x in range(0,24):
    #print("Hour: ",x ,len(GetData(None,1,x,x+1,"Monday")))
    MeasureMonday.append(len(GetData(None,1,x,x+1,"Monday")))
for x in range(0,24):
    #print("Hour: ",x ,len(GetData(None,1,x,x+1,"Sunday")))
    MeasureSunday.append(len(GetData(None,1,x,x+1,"Sunday")))

print(MeasureMonday)
print (MeasureSunday)






'''
print("Printing speed for class 1 through 9")

print(GetAverageSpeed(GetDataByClass(1)))
print(GetAverageSpeed(GetDataByClass(2)))
print(GetAverageSpeed(GetDataByClass(3)))
print(GetAverageSpeed(GetDataByClass(4)))
print(GetAverageSpeed(GetDataByClass(5)))
print(GetAverageSpeed(GetDataByClass(6)))
print(GetAverageSpeed(GetDataByClass(7)))
print(GetAverageSpeed(GetDataByClass(8)))
print(GetAverageSpeed(GetDataByClass(9)))

print("")
print("")

print("speed on days mon- sun")
print(GetAverageSpeed(GetDataByDayName("Monday")))
print(GetAverageSpeed(GetDataByDayName("Tuesday")))
print(GetAverageSpeed(GetDataByDayName("Wednesday")))
print(GetAverageSpeed(GetDataByDayName("Thursday")))
print(GetAverageSpeed(GetDataByDayName("Friday")))
print(GetAverageSpeed(GetDataByDayName("Saturday")))
print(GetAverageSpeed(GetDataByDayName("Sunday")))


print("Printing the average speed between 2 time intervals")
print(GetAverageSpeedInTimeInterval(6,14))
print(GetAverageSpeedInTimeInterval(7,9))

print("Prognosis over 24 hours car class 2 average speed")
for x in range(0,24):
    print("Hours: ", x, " - ",x+1 ,"\t", GetAverageSpeedInTimeInterval(x,x+1,GetDataByClass(2)))



print("Prognosis over 24 hours all car classes on mondays")
for x in range(0,24):
    print("Hours: ", x, " - ",x+1 ,"\t", GetAverageSpeedInTimeInterval(x,x+1,GetDataByDayName("Monday")))


print("Prognosis over 24 hours all car classes on Sundays")
for x in range(0,24):
    print("Hours: ", x, " - ",x+1 ,"\t", GetAverageSpeedInTimeInterval(x,x+1,GetDataByDayName("Sunday")))






    

#print(data[(data.dateTime.dt.hour>7) & (data.dateTime.dt.hour<10)])

#print(GetAverageSpeed(data[(data.dateTime.dt.hour>7) & (data.dateTime.dt.hour<10)]))




'''
    
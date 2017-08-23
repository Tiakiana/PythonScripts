import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import os as os
# visulaize the important characteristics of the dataset
import matplotlib.pyplot as plt

# step 1: download the data
dataframe_all = pd.read_table('C:\\Users\\jaarn\\Desktop\\Falen.txt')

print(dataframe_all.head())

dataframe_all.rename(columns = {'class' : 'cartype'}, inplace = True)
dataframe_all['datetime'] = pd.to_datetime(dataframe_all.datetime)


print(dataframe_all.columns)




isClass2 = dataframe_all.cartype == 2






isClass1 = dataframe_all.cartype == 1
isClass2 = dataframe_all.cartype == 2
isClass3 = dataframe_all.cartype == 3
isClass4 = dataframe_all.cartype == 4
isClass5 = dataframe_all.cartype == 5
isClass6 = dataframe_all.cartype == 6
isClass7 = dataframe_all.cartype == 7
isClass8 = dataframe_all.cartype == 8
isClass9 = dataframe_all.cartype == 9

class1data = dataframe_all[isClass1]
class2data = dataframe_all[isClass2]
class3data = dataframe_all[isClass3]
class4data = dataframe_all[isClass4]
class5data = dataframe_all[isClass5]
class6data = dataframe_all[isClass6]
class7data = dataframe_all[isClass7]
class8data = dataframe_all[isClass8]
class9data = dataframe_all[isClass9]

print(class1data.dtypes)



print(dataframe_all.shape)
print(class1data.shape)
print(class2data.shape)
print(class3data.shape)
print(class4data.shape)
print(class5data.shape)
print(class6data.shape)
print(class7data.shape)
print(class8data.shape)
print(class9data.shape)

print("")
print("------------------------------------------------------------------ gennemsnitshastigheder .---------------------------------------------------------------------")


counter = 0
for item in class1data.speed:
    counter = counter + item
print(counter/ len(class1data))

counter = 0
for item in class2data.speed:
    counter = counter + item
print(counter/ len(class2data))

counter = 0
for item in class3data.speed:
    counter = counter + item
print(counter/ len(class3data))

counter = 0
for item in class4data.speed:
    counter = counter + item
print(counter/ len(class4data))

counter = 0
for item in class5data.speed:
    counter = counter + item
print(counter/ len(class5data))

counter = 0
for item in class6data.speed:
    counter = counter + item
print(counter/ len(class6data))

counter = 0
for item in class7data.speed:
    counter = counter + item
print(counter/ len(class7data))

counter = 0
for item in class8data.speed:
    counter = counter + item
print(counter/ len(class8data))

counter = 0
for item in class9data.speed:
    counter = counter + item
print(counter/ len(class9data))

print("")


print("------------------------- Hvor mange kører for stærkt -------------------------------")
print("")
print("Class 1: ", (len(class1data[class1data.speed> 50])))
print("Hvilket ekvivalerer til ",  ((len(class1data[class1data.speed> 50]))/(len(class1data)))*100)
print("Class 2: " , len(class2data[class2data.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class2data[class2data.speed> 50]))/(len(class2data)))*100)
print("Class 3: " , len(class3data[class3data.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class3data[class3data.speed> 50]))/(len(class3data)))*100)
print("Class 4: " , len(class4data[class4data.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class4data[class4data.speed> 50]))/(len(class4data)))*100)
print("Class 5: " , len(class5data[class5data.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class5data[class5data.speed> 50]))/(len(class5data)))*100)
print("Class 6: " , len(class6data[class6data.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class6data[class6data.speed> 50]))/(len(class6data)))*100)
print("Class 7: " , len(class7data[class7data.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class7data[class7data.speed> 50]))/(len(class7data)))*100)
print("Class 8: " , len(class8data[class8data.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class8data[class8data.speed> 50]))/(len(class8data)))*100)
print("Class 9: " , len(class9data[class9data.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class9data[class9data.speed> 50]))/(len(class9data)))*100)

print("This is between 7 and 8 in the morning happenings")
#isClass8 = dataframe_all.cartype == 8

'''
Strålende eksempel som skal afkaste følgende.
Find noget på ugeday og time.

'''
'''
print("")


print("Hvor mange kører for stærkt på en mandag i lane 1?")
getmondays = class2data.datetime.dt.weekday_name == "Monday"
lane1 = class2data.lane == 1
lane2 = class2data.lane == 2

class2dataMondayAndLane1 = class2data[(lane1) & (getmondays)]
class2dataMondayAndLane2 = class2data[(lane2) & (getmondays)]
print("Class 2 i lane 1 der kører for stærkt: " , len(class2dataMondayAndLane1[class2dataMondayAndLane1.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class2dataMondayAndLane1[class2dataMondayAndLane1.speed> 50]))/(len(class2dataMondayAndLane1)))*100)
print("Class 2 i lane 2 der kører for stærkt: " , len(class2dataMondayAndLane2[class2dataMondayAndLane2.speed> 50]))
print("Hvilket ekvivalerer til ",  ((len(class2dataMondayAndLane2[class2dataMondayAndLane2.speed> 50]))/(len(class2dataMondayAndLane2)))*100)
'''


print("")
print (class2data.datetime.dt.hour)



'''
print[class2data.datetime.dt.hour]
ts =class2date[class2data.datetime.dt.hour>7 & class2data.datetime.dt.hour<9]
'''




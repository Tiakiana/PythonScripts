import pandas as pd

'''
data = pd.read_csv(io.StringIO(sys.argv[1]))
print(data.dtype)
data['dateTime'] = pd.to_datetime(data.dateTime)
'''

data = pd.read_csv('C:\\Users\\jaarn\\Desktop\\Falencsv.txt',sep =";",index_col = "datetime")
#data = pd.read_csv(io.StringIO(sys.argv[1]))
#data['datetime'] = pd.to_datetime(data.datetime)
#data.rename(columns = {'class' : 'cartype'}, inplace = True)
print(data.head())
data.drop('siteid',axis = 1, inplace = True)
data.drop('vehicleid',axis = 1, inplace = True)
data.drop('lane',axis = 1, inplace = True)
data.drop('length',axis = 1, inplace = True)
data.drop('class',axis = 1, inplace = True)
data.drop('wrong_dir',axis = 1, inplace = True)
#print(data.head())

#data.set_index(data.datetime, inplace = True)
print(data.head())

print(data.columns)
data.to_csv('C:\\Users\\jaarn\\Desktop\\Falencsv2.txt',",")
print("conversion done")




import pandas as pd
import requests
import sys
from sklearn import linear_model

data = pd.read_table('C:\\Users\\jaarn\\Desktop\\Falenmaj.txt')
data['datetime'] = pd.to_datetime(data.datetime)

pd.Index(data.datetime);

print(data.head())
X = data.datetime
y = data.speed

print(X.shape)
print(y.shape)
regr =  linear_model.LinearRegression()
regr.fit(X,y)
print(regr.score(X,y))




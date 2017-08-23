import requests
import pandas as pd



#parameters = {"from": "2017-07-18 00:00:00", "to": "2017-07-20 00:00:00"}
response = requests.get("http://apps.odense.dk/data/newtags/115-dk-full.json")
print(response.status_code)
data = pd.read_json(response.content)
#print(data.head(1))
print("")
print("")
print("")
print("")
#print(data.columns)
print("")
print("")
print("")

#print(data.columns)
#print(data.type)
#print(data.features)

print(data.features.to_frame().properties)


'''
print(data.columns)
things = data.features.apply(pd.Series)
print(things.columns)
feature = data.features.to_frame()

print(feature.columns)

thishere = feature.features.apply(pd.Series)
print(thishere.columns)
props = thishere.properties.apply(pd.Series)

prop19 = props.prop19.apply(pd.Series)
print(prop19.columns)



#print(thishere.head)

#print(feature.)

#print("shape is: ",data.shape)

'''

#

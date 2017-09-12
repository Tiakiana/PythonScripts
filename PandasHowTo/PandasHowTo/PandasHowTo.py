import pandas as pd


#Indhent data fra skrivebord. Separeret af semicolon og indexeret på date time
data = pd.read_csv('C:\\Users\\jaarn\\Desktop\\Falencsv.txt',sep =";",index_col = "datetime")

#Indlæs argumenter, hvis du kører scriptet fra eksempelvis C#
data = pd.read_csv(io.StringIO(sys.argv[1]))

# gør date time til datetime formatet indbygget i Pandas
data['datetime'] = pd.to_datetime(data.datetime)

#Laver en renaming af en given kollonne
data.rename(columns = {'class' : 'cartype'}, inplace = True)

# dropper en given kolonne. inplace gør at vi ændrer direkte på datasettet.
data.drop('siteid',axis = 1, inplace = True)

#printer dataen til en .csv fil, og angiver at datapunkterne skal separeres med et komma.
data.to_csv('C:\\Users\\jaarn\\Desktop\\Falencsv2.txt',",")


#Kommandoer til datasettet
#Agg sammenhæfter info der er blevet bestilt med en string.
print(data.groupby(data.cartype).speed.agg(["count","min","max","mean"]))
#Groupby sørger for at al dataen forefindes i forskellige grupper.

#viser de 5 øverste datapunkter med deres kolonne navne
print(data.head())





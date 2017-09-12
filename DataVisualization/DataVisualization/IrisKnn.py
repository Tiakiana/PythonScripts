from sklearn.datasets import load_iris



iris = load_iris()

X = iris.data

y = iris.target

print(X.shape)
print(y.shape)


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)

print(knn.predict([3,5,4,2]))
x_new = [[3,5,4,2],[5,4,3,2]]
print (knn.predict(x_new))

print("Laver nye predictions med en lineær model")

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X,y)
print(logreg.predict(x_new))

print("test de to typer algoritmer")

KNNyres = knn.predict(X)
logRes = logreg.predict(X)

from sklearn import metrics
print("Knn score")
print (metrics.accuracy_score(y,KNNyres))
print("log score")
print(metrics.accuracy_score(y,logRes))


#Hello World - Machine Learning Recipes #1Google Developers

# El codigo proviene de https://www.youtube.com/watch?v=cKxRvEZd3Mw y este se comparte para aprender sobre Machine Learning

# Nuestra primer programa de Machine Learning, para esto necesitamos instalar https://www.anaconda.com/download/#linux 
# Dependiendo de nuestro sistema operativo descargamos el archivo correspondiente y lo instalamos de lo contrario no va funcionar al correr e archivo de python 

# santoslopez@usuario: hello-world.py 

# debido a que si usamos unicamente python (no trae digamos que librerias para que funcione Machine Learning)


import sklearn import tree 

#features = [[140,"smooth"],[130,"smooth"],[150,"bumpy"],[170,"bumpy"]]

#labels = ["apple","apple","orange","orange"]

features = [[140,1],[130,1],[150,0],[170,0]]

labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features,labels)

print clf.predict([[]])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading iris dataset into dataframe df
df = pd.read_csv('iris.csv')

#filtering the dataset to seperate the 3 species for plotting
setosa = df[df['species'] == 'Iris-setosa']
versicolor = df[df['species'] == 'Iris-versicolor']
virginica = df[df['species'] == 'Iris-virginica']

#scatter plot for sepal length vs petal length for the 3 species in the dataset
plt.scatter(setosa['sepal_length'], setosa['petal_length'], color="red", alpha=0.5, label="Iris setosa")
plt.scatter(versicolor['sepal_length'], versicolor['petal_length'], color="green", alpha=0.5, label="Iris versicolor")
plt.scatter(virginica['sepal_length'], virginica['petal_length'], color="blue", alpha=0.5, label="Iris virginica")

#title and axis names
plt.title("sepal Length vs petal Length")
plt.xlabel("sepal length (cm)")
plt.ylabel("petal length (cm)")
plt.legend(loc="lower right")

#show scatter plot
plt.show()

#scatter plot for sepal width vs petal width for the 3 species in the dataset
p2 = plt
p2.scatter(setosa['sepal_width'], setosa['petal_width'], color="red", alpha=0.5, label="Iris setosa")
p2.scatter(versicolor['sepal_width'], versicolor['petal_width'], color="green", alpha=0.5, label="Iris versicolor")
p2.scatter(virginica['sepal_width'], virginica['petal_width'], color="blue", alpha=0.5, label="Iris virginica")

p2.title("sepal width vs petal width")
p2.xlabel("sepal width (cm)")
p2.ylabel("petal width (cm)")
p2.legend(loc="best")

#show scatter plot
p2.show()

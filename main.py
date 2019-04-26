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
plt.title("Sepal Length vs Petal Length")
plt.xlabel("sepal length (cm)")
plt.ylabel("petal length (cm)")

#show scatter plot
plt.show()
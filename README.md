# Iris Flower Data Set Project

## Introduction
The goal of this project is to investigate the famous Iris flower dataset and find interesting observations through the use of Python
and related tools. The Iris flower data set is a classic dataset that is traditionally used for classification and prediction i.e. to see
which features of the Iris can identify the flower to be a specific type of Iris. The data set is also frequently used in the world of computing and data science.

The data set was first introduced by the well-known statistician and biologist Ronald Fischer in 1936, it consists of 50 samples each from
the following 3 species of Iris flower: Iris setosa, Iris versicolor and Iris virginica. Each sample has 4 features measured in centimetres:
petal width, petal length, sepal width and sepal length.

## Tools and Libraries
I investigated the data set using Python 3.7.3 and some Python libraries, these libraries are:
* [pandas](https://pandas.pydata.org/)
* [numpy](https://www.numpy.org/)
* [matplotlib](https://matplotlib.org/)

Pandas is a library that is used for data manipulation and analysis. It allowed me to read the dataset from the csv file directly into a DataFrame, pandas also
has the capability of filtering the data into different sections e.g. analysing only Iris setosa data.

Numpy is a library that provides easy to use functions for mathematical operations such as getting the maximum value of an array i.e. a column of data.

Matplotlib is a library which is capable of producing various types of graphs, charts and plots. I use it to visualise some of the data and plot some features against others. The plots are found further down.

## Running iris.py
To run the script located in iris.py, you must have pandas, numpy and matplotlib installed. Guides to installing these libraries are found on their websites. The script can be run from the python shell or even a code editor with a python interpreter. For the dataset to be read correctly, the iris.csv file must be located in the same directory as iris.py.

## Investigating the Dataset
To analyse this dataset, I wrote a python script iris.py that generates tables of data which show the maximum, minimum, the mean, and the standard deviation of each feature (petal and sepal length/width). Numpy is used to get all the values for the table and pandas creates the table itself.

The script also generates 3 graphs, using matplotlib to plot the data framed by pandas. 
The first graph is a scatter plot which plots sepal length vs petal length for all 3 species.
![Figure 1](https://github.com/ildaro/Iris-Flower/blob/master/figures/sepal_v_petal_length.png)

The second graph is also a scatter plot which plots sepal width vs petal width for all 3 species. 
![Figure 2](https://github.com/ildaro/Iris-Flower/blob/master/figures/sepal_v_petal_width.png)

The final graph is a bar plot, which plots the mean values of all 4 features for each of the 3 species.
![Figure 3](https://github.com/ildaro/Iris-Flower/blob/master/figures/barplot.png)


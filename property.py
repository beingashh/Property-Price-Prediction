import numpy
import matplotlib.pyplot as plot
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv('C:\python\property.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values
linearRegressor = LinearRegression()
linearRegressor.fit(X, Y)
yPred = linearRegressor.predict(X)
plot.scatter(X,Y, color = 'red')
plot.plot(X, yPred, color = 'blue')
plot.scatter(X, yPred, color = 'blue')
plot.title('Property Prices Prediction')
plot.xlabel('Property(Sq Ft)')
plot.ylabel('Prices')
plot.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 23:39:21 2020

@author: paul
"""

import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('bombardier_revenue.csv')
plt.scatter(data['Year'], data['Revenue'])
plt.show()
model = LinearRegression()
model.fit(data[['Year']], data[['Revenue']]) 
print(model.predict([[2020]]))
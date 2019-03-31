# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:42:31 2019

@author: shradhamallik
"""

#Importing the libraries
import numpy as np
import pandas as  pd

#importing the dataset
dataset = pd.read_excel('Data.xlsx')

#Classifying into independent and dependent variables
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

print(X)
print(Y)

#Handle missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy="mean")
imputer = imputer.fit(X[:, 1:3])
X[:,1:3] = imputer.transform(X[:, 1:3])

print(X)
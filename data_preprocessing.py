from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Importing the libraries
import numpy as np
import pandas as pd

# importing the dataset
dataset = pd.read_excel('Data.xlsx')

# Classifying into independent and dependent variables
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# Handling missing values
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding categorical values

X_le = LabelEncoder()
X[:, 0] = X_le.fit_transform(X[:, 0])


Y_le = LabelEncoder()
Y = Y_le.fit_transform(Y)


X_ohe = OneHotEncoder(categorical_features=[0])
X = X_ohe.fit_transform(X).toarray()

# Spliting dataset into training and test set
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=0)

# Feature scaling
X_sc = StandardScaler()
X_train = X_sc.fit_transform(X_train)
X_test = X_sc.fit_transform(X_test)

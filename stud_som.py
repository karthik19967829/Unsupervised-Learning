# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:09:39 2017

@author: Akhilesh
"""



# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('example1.csv')
X = dataset.iloc[::].values

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

# Training the SOM
from minisom import MiniSom
som = MiniSom(x = 20, y = 20, input_len = 16, sigma = 1.0, learning_rate = 0.5)
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 100)
'''from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()

X = dataset.iloc[:,:11].values
y = dataset.iloc[:, 11].values
X=sc.fit_transform(X)
y=sc.fit_transform(y)
X=np.reshape(X,(154,1,11))'''

# Encoding categorical data
'''from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]'''
from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
colorbar()
show()

mapping=som.win_map(X)
gang=np.array(mapping[(9,10)])
gang=sc.inverse_transform(gang)
gang1=np.array(mapping[(9,11)])
gang1=sc.inverse_transform(gang1)
'''# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)

# Feature Scaling
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

regressor=Sequential()
regressor.add(LSTM(units=20,activation='sigmoid',input_shape=(None,11)))
regressor.add(Dense(units=1))
regressor.compile(optimizer='adam',loss='mean_squared_error')
regressor.fit(X_train,y_train,batch_size=32,epochs=2000)





predicted=regressor.predict(X_test)
predicted=sc.inverse_transform(predicted)
y_test=sc.inverse_transform(y_test)
from sklearn.metrics import mean_squared_error
RMSE = mean_squared_error( predicted,y_test)**0.5'''

'''compare y_test and predicted to get an underdtand the prediction'''






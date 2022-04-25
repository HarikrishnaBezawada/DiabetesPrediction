# -*- coding: utf-8 -*-
"""AI Mid Dense 1 A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15HdvR5pcyiPn81vSptOE34aepFZPWPOB

This is build on Dense layer : Multi Layer Perceptron

Lets Import all the necessary Libraries
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.callbacks import TensorBoard
from keras import optimizers
import time
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn import model_selection
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

"""Loaded the Dataset here & Display header info"""

!pip install seaborn

import seaborn as sns

df = pd.read_csv ('diabetes.csv',encoding='utf-8')
print(df.head())

"""Lets Build relation b/w every variable from dataset & analyze"""

X =df[['Pregnancies',	'Glucose'	,'BloodPressure',	'SkinThickness',	'Insulin',	'BMI',	'DiabetesPedigreeFunction'	,'Age',	'Outcome']]
dim=X.shape[1]

foo = sns.heatmap(X.corr(), vmax=1, square=True, annot=True)
plt.figure(figsize=(28,28))
X=X.to_numpy()
Y= df[['Outcome']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D
x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.02)

y_train2=tf.keras.utils.to_categorical(y_train)
print(y_train2.shape)
category=2      
y_test2=tf.keras.utils.to_categorical(y_test, num_classes=(category))

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=90, activation=tf.nn.relu, input_dim=dim))
model.add(tf.keras.layers.Dense(units=100, activation=tf.nn.relu ))
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax ))
model.compile(optimizer='adam', loss=tf.keras.losses.categorical_crossentropy, metrics=['accuracy'])
history=model.fit(x_train, y_train2, epochs=170, batch_size=80)

model.summary()

"""Lets evaluate algorithm by using this loss & accuracy graphical values"""

pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1) # set the vertical range to [0-1]
plt.show()

score = model.evaluate(x_test, y_test2 )
print("score:",score)

predict2 = model.predict(x_test)
print("predict_classes:",predict2)
print("y_test",y_test[:])

# Serialize weights to HDF5
model.save_weights("UCMmodel.h5")
print ("Saved model")


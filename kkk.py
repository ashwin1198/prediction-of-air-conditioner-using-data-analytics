import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,confusion_matrix
from flask import Flask,abort,jsonify,request
from sklearn.externals import joblib
import pickle
from sklearn import preprocessing,cross_validation,svm,neighbors
from collections import Counter
dff=pd.read_csv('D:\Downloads\dataser.csv')
X=np.array(dff[['KWH','NHSLDMEM','MONEYPY','BTUEL']])
y=np.array(dff['AIRCOND'])

x_train,x_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2,stratify=y)

from sklearn.neighbors import KNeighborsClassifier
neighac=KNeighborsClassifier(n_neighbors=3,weights='distance')
neighac.fit(x_train,y_train)
y_pred=neighac.predict(x_test)
#joblib.dump(neighac,'ac.pkl')
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_pred,y_test))
""""
print(neighac.predict([[0,0,0,0]]))
print(neighac.predict([[5015,5,3,5015*3.142]]))
print(neighac.predict([[3305,3,4,3305*3.142]]))
print(neighac.predict([[963,5,6,963*3.142]]))
print(neighac.predict([[1707,6,8,1707*3.142]]))
print(neighac.predict([[2875,19,2,2875*3.412]]))
"""

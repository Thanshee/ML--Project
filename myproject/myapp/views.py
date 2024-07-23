from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import requests
import pandas as pd
import numpy as np

# Create your views here.
def index(request):
    return render(request,'index.html')

def ferti(request):
    return render(request,'fertilizer.html')

def predict(request):
    data = pd.read_csv("C:\\Users\\Thansheer\\Downloads\\fertilizerprediction.csv")
    data=data.drop(['Temparature'], axis = 1)
    data=data.drop(['Moisture'], axis = 1)
    data=data.drop(['Soil Type'], axis = 1)
    X = data.drop(['Fertilizer Name'], axis=1)
    Y = data['Fertilizer Name']
    Numerics=LabelEncoder()
    X['Crop_n'] = Numerics.fit_transform(X['Crop Type'])
    X_n = X.drop(['Crop Type'], axis=1)
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X_n, Y, test_size = 0.2)
    model = GaussianNB()
    model.fit(Xtrain, Ytrain)
    var1 = float(request.GET['N'])
    var2 = float(request.GET['K'])
    var3 = float(request.GET['P'])
    var4 = float(request.GET['R'])
    var5 = Numerics.fit_transform([request.GET['C']])[0]
    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1,-1))
    label = "The suitable fertilizer is: " + str(pred[0])
    return render(request,'fertilizer.html', {'result': label})
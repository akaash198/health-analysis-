from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Create your views here.
def index(request):
    return render(request,'app/index.html')
def home(request):
    return render(request,'app/home.html')
def predict(request):
    return render(request,'app/predict.html')
def about(request):
    return render(request,'app/about.html')
def contact(request):
    return render(request,'app/contact.html')
def result(request):
    data = pd.read_excel(r'C:\Users\akaas\Desktop\sandhya\static\dataset1.xlsx')
    data['PULSE']=data['PULSE'].fillna(data['PULSE'].median())
    data['SpO2']=data['SpO2'].fillna(data['SpO2'].median())
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    classifier.fit(X_train, y_train)
    val1=float(request.GET['n1'])
    val2=float(request.GET['n2'])
    val3=float(request.GET['n3'])
    val4=float(request.GET['n4'])
    val5=float(request.GET['n5'])
    val6=float(request.GET['n6'])
    val7=float(request.GET['n7'])
  
    pred=classifier.predict([[val1,val2,val3,val4,val5,val6,val7]])
    result1=""
    if pred==[1]:
        result1="Sorry, you are not able to travel.Please go to the doctor for further details.Because, you may have shortness of breathe or blood clots in some parts of your body.."
        return render(request,'app/predict.html',{"result2":result1})
         
    else:
        result1="Happy to say that you can travel!!!"
        return render(request,'app/predict.html',{"result2":result1})



from django.shortcuts import render
import joblib
import os
import json
import pandas as pd
from .models import churn_prediction
import psycopg2


# Create your views here.

def index(request):
    return render(request,'index.html')

def result(request):
    model = joblib.load('../prediction_service/model/model.joblib')
    list = []
    list.append(float(request.GET['CreditScore']))
    list.append(float(request.GET['Gender']))
    list.append(float(request.GET['Age']))
    list.append(float(request.GET['Tenure']))
    list.append(float(request.GET['Balance']))
    list.append(float(request.GET['NumOfProducts']))
    list.append(float(request.GET['HasCrCard']))
    list.append(float(request.GET['IsActiveMember']))
    list.append(float(request.GET['EstimatedSalary']))
    answer = model.predict([list]).tolist()[0]

    b = churn_prediction(CreditScore=request.GET['CreditScore'],Gender=request.GET['Gender'],Age=request.GET['Age'],Tenure=request.GET['Tenure'],Balance=request.GET['Balance'],NumOfProducts=request.GET['NumOfProducts'],HasCrCard=request.GET['HasCrCard'],IsActiveMember=request.GET['IsActiveMember'],EstimatedSalary=request.GET['EstimatedSalary'],Exited=answer)
    b.save()

    return render(request,"index.html",{'answer':answer})

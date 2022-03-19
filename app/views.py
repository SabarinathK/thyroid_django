from django.shortcuts import render
import joblib as jb
import numpy as np
from pathlib import Path

# Create your views here.
def home(request):
    return render (request,'index.html')

def prediction(request):
    if request.method=='POST':
        TSH=request.POST['TSH']
        FTI=request.POST['FTI']
        TT4=request.POST['TT4']
        T3=request.POST['T3']
        query_hypothyroid=request.POST['query_hypothyroid']
        on_thyroxine=request.POST['on_thyroxine']
        sex=request.POST['sex']
        pregnant=request.POST['pregnant']
        psych=request.POST['psych']
        
        arr=np.array([[TSH,FTI,TT4,T3,query_hypothyroid,on_thyroxine,sex,pregnant,psych]])
    
        model=jb.load('thyroid/model/model_RandomForest.pkl')
        result= model.predict(arr)
        if result ==1:
            return render(request,'after.html',{'data':'your value are abnormal and are have thyroid'})
        else :
            return render(request,'after.html',{'data':'your value are normal '})
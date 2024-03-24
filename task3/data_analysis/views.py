from django.shortcuts import render

from django.http import HttpResponse
from api import fetch_api_data

def index(request):
    data, label = fetch_api_data()
    context = {
        'data':data,
        'label':label
    }
    return render(request,'pages/index.html',context)
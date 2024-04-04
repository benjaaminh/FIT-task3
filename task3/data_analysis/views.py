from django.shortcuts import render

from django.http import HttpResponse
from api import fetch_api_data
from csvreader import read_csv_file
def index(request):
    data, label = fetch_api_data()
    csvdata = read_csv_file()
    context = {
        'data':data,
        'label':label,
        'csvdata':csvdata
    }
    return render(request,'pages/index.html',context)
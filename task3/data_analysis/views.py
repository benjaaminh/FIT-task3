from django.shortcuts import render

from django.http import HttpResponse
from api import fetch_api_data
from csvreader import read_csv_file
def index(request):
    data = fetch_api_data()
    csvdata = read_csv_file()
    context = {
        'data':data,
        'csvdata':csvdata,
        'combined_data':zip(data,csvdata)
    }
    return render(request,'pages/index.html',context)
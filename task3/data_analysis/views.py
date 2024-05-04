from django.shortcuts import render

from django.http import HttpResponse
from api import fetch_api_data
from csvreader import read_csv_file
def index(request):
    apidata = fetch_api_data() #api data
    csvdata = read_csv_file() #csv data
    context = { #pass the context to the template
        'api_data':apidata,
        'csvdata':csvdata,
        'combined_data':zip(apidata,csvdata) #combined data is a tuple of both datasets
    }
    return render(request,'pages/index.html',context) #render template
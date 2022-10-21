import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'name':'Prathmesh'})

def verify(request):
    return HttpResponse("Verify Page")

def getData(request):

    uname = request.POST['name']
    sname = request.POST['surname']

    data = uname+sname

    return render(request, 'index.html', {"data":data, 'name':'Prathmesh'})

import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def verify(request):
    return HttpResponse("Verify Page")
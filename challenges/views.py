from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Jan(request):
    return HttpResponse("This is month January  ")    

def Feb(request):
    return HttpResponse("This is month Feburary")
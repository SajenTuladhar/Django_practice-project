from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def Jan(request):
    return HttpResponse("This is month January  ")    

def Feb(request):
    return HttpResponse("This is month Feburary")

def monthly_challenges(request, month):
    challenge_text= None
    if month == "January":
        challenge_text = "Learn a new language"
    elif month == "Febuary":
        challenge_text = "Learn to read music"
    elif month == "March":
        challenge_text  = "Climb Mount Rushmore"
    else:
        return HttpResponseNotFound("This does not exist,404 error")
    
    return HttpResponse(challenge_text)
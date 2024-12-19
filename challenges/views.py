from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
# Create your views here.


monthly_challenges= {
    "january":"Learn a new language",
    "febuary":"draw more",
    "march":"read more books",
    "april":"learn to fight",
    "may":"learn music",
    "june":"workout",
    "july":"help someone",
    "august":"save someone",
    "september":"help random stranger",
    "october":"learn to fly",
    "november":"climb mount everst",
    "december":"Learn Django",
}

def monthly_challenge_by_number(request, month):
    months= list(monthly_challenges.keys())
    
    redirect_month= months[month-1]
    return HttpResponseRedirect("challenges/"+redirect_month)

def monthly_challenge(request, month):
    challenge_text= monthly_challenges[month]
    return HttpResponse(challenge_text)
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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

def monthly_challenge(request, month):
    challenge_text= monthly_challenges[month]
    return HttpResponse(challenge_text)
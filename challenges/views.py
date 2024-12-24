from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string  


# Create your views here.

monthly_challenges= {
    "january":"Learn a new language",
    "febuary":"draw more",
    "march":"read more books",
    "april":"learn to fight",
    "may":"learn music",
    "june":"workout",
    "july":"Own a new phone",
    "august":"save someone",
    "september":"help random stranger",
    "october":"learn to fly",
    "november":"climb mount everst",
    "december": None,
}

def index(request):
    months = list(monthly_challenges.keys())
    return render (request, "challenges/index.html",{
        "months" : months
    })

def monthly_challenge_by_number(request, month):
    months= list(monthly_challenges.keys())
    
    if month > len (months):
        return HttpResponseNotFound("invaild month")
    
    redirect_month= months[month-1]
    redirect_path = reverse("month-challenge",args= [redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month): 
    try:
        challenge_text= monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "month" : month,
            "challenge": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>this month is not supported<h1>")
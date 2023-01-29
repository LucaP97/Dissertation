from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    return render(request, "tss/home.html")

def about(request):
    return render(request, "tss/about.html")

def contact(request):
    return render(request, "tss/contact.html")

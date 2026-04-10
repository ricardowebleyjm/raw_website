from django.shortcuts import render
from django.http import HttpRequest

def home(request: HttpRequest):
    return render(request, 'a_core/home.html')

def contact(request: HttpRequest):
    return render(request, 'a_core/contact.html')

def projects(request: HttpRequest):
    return render(request, 'a_core/projects.html')

def portfolio(request: HttpRequest):
    return render(request, 'a_core/portfolio.html')
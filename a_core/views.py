from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from .models import Project
from .forms import ContactForm
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

@cache_page(60 * 5) 
def home(request: HttpRequest):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    return render(request, 'a_core/home.html', {'projects': featured_projects})

@vary_on_headers("Cookie")
@cache_page(60 * 2)
def contact(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please check the fields and try again.')
    else:
        form = ContactForm()
        
    return render(request, 'a_core/contact.html', {'form': form})

@cache_page(60 * 5) 
def projects(request: HttpRequest):
    all_projects = Project.objects.prefetch_related('skills').all()
    return render(request, 'a_core/projects.html', {'projects': all_projects})

@cache_page(60 * 5) 
def portfolio(request: HttpRequest):
    return redirect('projects')
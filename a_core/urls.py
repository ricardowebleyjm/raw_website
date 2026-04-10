
from django.urls import path
from a_core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('portfolio/', views.portfolio, name='portfolio'),
]

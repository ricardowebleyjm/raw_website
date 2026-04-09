
from django.urls import path
from a_core import views

urlpatterns = [
    path('', views.home, name='home'),
]

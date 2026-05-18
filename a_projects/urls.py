from django.urls import path
from . import views

urlpatterns = [
    path('api/list/', views.ProjectList.as_view(), name='project-list'),
]
from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.core.cache import cache

from a_core.views import projects

from .models import Project


class ProjectList(View):
    """
    A class-based view that returns a list of projects in JSON format.
    """
    
    def get(self, request, *args, **kwargs):
        cache_key = 'project_list_data'
        data = cache.get(cache_key)
        print(f"Cache hit: {data is not None}")

        if data is None:
            projects = Project.objects.all()
            data = list(projects.values(
                'id', 'name', 'slug', 'description', 
                'featured', 'cover_image', 'created_at'
            ))
            cache.set(cache_key, data, 60 * 15)
        return JsonResponse(data, safe=False)


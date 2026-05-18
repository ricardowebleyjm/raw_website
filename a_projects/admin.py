from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Project model.
    """
    
    list_display = ('name', 'featured', 'created_at', 'updated_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('featured',)

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'description', 'content')
        }),
        ('Media & Links', {
            'fields': ('cover_image', 'live_link', 'repo_link')
        }),
        ('Settings', {
            'fields': ('featured',)
        }),
    )
from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    cover_image = models.ImageField(upload_to='projects/%Y/%m/%d/', null=True, blank=True)
    description = models.TextField()
    content = models.TextField(help_text="Detailed markdown or HTML content", blank=True)
    featured = models.BooleanField(default=False)
    live_link = models.URLField(max_length=255, blank=True, null=True)
    repo_link = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
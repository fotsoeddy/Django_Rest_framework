from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # For blog images
    tags = models.CharField(max_length=255, blank=True)  # For tags (e.g., "tech, programming")
    category = models.CharField(max_length=100, blank=True)  # For category (e.g., "Technology")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
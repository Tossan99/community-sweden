from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PeerReview(models.Model):

    """
    Model for user posts
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts")
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(max_length=5000, blank=True)
    excerpt = models.TextField(max_length=150, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Written by {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug:
            """
            Generate a unique slug based on the title and timestamp
            """
            base_slug = slugify(self.title)
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            unique_slug = f"{base_slug}-{timestamp}"
            self.slug = unique_slug

        super().save(*args, **kwargs)
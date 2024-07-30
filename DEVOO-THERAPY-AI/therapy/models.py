from django.db import models
from django.contrib.auth.models import User

class Therapist(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True) 

    def __str__(self):
        return self.title

class CommunityMessage(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}"

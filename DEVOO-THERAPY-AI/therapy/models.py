from django.db import models

class Therapist(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    website = models.URLField(blank=True)

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(blank=True)

class CommunityMessage(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

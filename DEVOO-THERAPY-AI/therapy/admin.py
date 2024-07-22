from django.contrib import admin
from .models import Therapist, Exercise, CommunityMessage

# Register your models here.
admin.site.register(Therapist)
admin.site.register(Exercise)
admin.site.register(CommunityMessage)

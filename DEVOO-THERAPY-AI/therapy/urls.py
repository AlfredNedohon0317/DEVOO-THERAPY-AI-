from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TherapistViewSet, ExerciseViewSet, CommunityMessageViewSet
from django.contrib import admin


router = DefaultRouter()
router.register(r'therapists', TherapistViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'community_messages', CommunityMessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('therapy.urls')),
]

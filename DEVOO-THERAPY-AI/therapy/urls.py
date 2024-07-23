from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TherapistViewSet, ExerciseViewSet, CommunityMessageViewSet, signup

router = DefaultRouter()
router.register(r'therapists', TherapistViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'community_messages', CommunityMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
]




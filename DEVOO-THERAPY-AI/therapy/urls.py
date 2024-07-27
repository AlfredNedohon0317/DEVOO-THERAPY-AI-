#therapy/urls.py 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'therapists', views.TherapistViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'community_messages', views.CommunityMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.signup, name='signup'),
    path('generate-response/', views.generate_response, name='generate-response'),
    path('update_account/', views.update_account, name='update_account'),
    path('delete_account/', views.delete_account, name='delete_account'),
]

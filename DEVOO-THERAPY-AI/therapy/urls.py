from django.urls import path
from . import views

urlpatterns = [
    path('therapists/', views.TherapistViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('exercises/', views.ExerciseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('community_messages/', views.CommunityMessageViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('signup/', views.signup, name='signup'),
    path('generate-response/', views.generate_response, name='generate-response'),
    path('update_account/', views.update_account, name='update_account'),  # Update account route
    path('delete_account/', views.delete_account, name='delete_account'),  # Delete account route
]

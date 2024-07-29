"""
URL configuration for therapy_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# #therapy_api/urls.py 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('api/', include('therapy.urls')),  # Therapy app API routes
    path('api/auth/', include('dj_rest_auth.urls')),  # Authentication routes provided by dj_rest_auth
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration routes provided by dj_rest_auth
]


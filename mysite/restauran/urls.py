from rest_framework import routers
from .models import *
from django.urls import path, include

routers = routers.DefaultRouter()

urlpatterns = [
    path('', include(routers.urls)),
]
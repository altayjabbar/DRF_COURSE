# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),  # This should map the /api/ route to the api_home view
]

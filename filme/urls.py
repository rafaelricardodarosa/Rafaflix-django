from django.urls import path, include
from .views import Homepage, Homefilmes

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
]
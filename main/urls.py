from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('genre/<int:genre_id>', get_genre, name='genre'),
    path('film/<int:pk>/', film_detail, name='film_detail'),
]

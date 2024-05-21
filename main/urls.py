from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('genre/<int:pk>/', GenreView.as_view(), name='genr'),
    path('index/', FilmList.as_view(), name='film'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
]

from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('films', FilmViewSet, basename='films')

urlpatterns = [
    path('', FilmList.as_view(), name='home'),
    path('genre/<int:pk>/', GenreView.as_view(), name='genr'),
    path('index/', FilmList.as_view(), name='film'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('api/', Film.as_view(), name='home'),
]

urlpatterns += router.urls

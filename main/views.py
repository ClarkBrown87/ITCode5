from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from main import models


def index(request):
    films = models.Film.objects.all()
    genres = models.Genre.objects.all()

    context = {'film': films,
               'genres': genres,
               'title': 'Список фильмов',
               }

    return render(request, template_name='main/index.html', context=context)


def get_genre(request, genre_id):
    films = models.Film.objects.filter(genre=genre_id)
    genres = models.Genre.objects.all()
    genre = models.Genre.objects.get(pk=genre_id)

    context = {'film': films,
               'genres': genres,
               'genre': genre,
               }

    return render(request, template_name='main/genre.html', context=context)


def film_detail(request, pk):
    book = models.Film.objects.get(pk=pk)
    context = {'book': book}

    # Отображаем шаблон с информацией о книге
    return render(request, template_name='main/film_detail.html', context=context)

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView

from main import models


class FilmList(ListView):
    model = models.Film
    context_object_name = "film"
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        genre = models.Genre.objects.all()

        context["title"] = 'Список фильмов'
        context["genres"] = genre

        return context


class FilmDetailView(DetailView):
    model = models.Film
    context_object_name = "film"
    template_name = 'main/film_detail.html'


class GenreView(DetailView):
    model = models.Genre
    context_object_name = "gen"
    template_name = 'main/genre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre_id = self.kwargs['pk']
        book = models.Film.objects.filter(genre=genre_id)
        genre = models.Genre.objects.get(pk=genre_id)
        genres = models.Genre.objects.all()

        context['film'] = book
        context['genre'] = genre
        context['genres'] = genres

        return context


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

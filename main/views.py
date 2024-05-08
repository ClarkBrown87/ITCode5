from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from main import models


def index(request):
    film = models.Film.objects.all()

    context = {'film': film,
               'title': 'Список фильмов',
               }

    return render(request, template_name='main/index.html', context=context)

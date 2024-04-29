from django.http import HttpResponse
from django.utils import timezone


def index(request):
    now = timezone.localtime(timezone.now())
    format_now = now.strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f'Текущая дата и время {format_now}')

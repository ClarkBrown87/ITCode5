import django_filters
from main import models


class Film(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Название', lookup_expr='icontains')

    public_date__gt = django_filters.DateFilter(field_name='public_date', lookup_expr='gt', label='Дата выпуска от')
    public_date__lt = django_filters.DateFilter(field_name='public_date', lookup_expr='lte', label='Дата выпуска до')

    revenue__gt = django_filters.NumberFilter(field_name='revenue', lookup_expr='gt', label='Выручка от')
    revenue__lt = django_filters.NumberFilter(field_name='revenue', lookup_expr='lte', label='Выручка до')

    class Meta:
        model = models.Film
        exclude = ('director', 'description', 'public_date', 'revenue', 'photo',)

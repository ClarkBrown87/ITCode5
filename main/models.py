from django.db import models
from django.urls import reverse


class User(models.Model):
    POSITION = (
        ('User', 'Пользователь'),
        ('Worker', 'Сотрудник'),
        ('Admin', 'Админ')
    )

    first_name = models.CharField('Имя', max_length=100, default='')
    last_name = models.CharField('Фамилия', max_length=100, default='')
    patronynic = models.CharField('Отчество', max_length=100, blank=True)
    email = models.EmailField('Электронная почта', unique=True)
    phone = models.CharField('Телефон', max_length=20, blank=True, null=True, unique=True)
    date_birth = models.DateField('День рождения', default="2002-10-01")
    position = models.CharField('Доступ', max_length=100, choices=POSITION, default='User')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Film(models.Model):
    name = models.CharField("Название фильма", max_length=50)
    director = models.CharField("Режиссер", max_length=50)
    description = models.TextField('Описание', blank=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр', null=True, blank=True)
    public_date = models.DateField('Дата выпуска', blank=True, null=True)
    revenue = models.DecimalField('Выручка', max_digits=10, decimal_places=2, default='0.00')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('film_detail', args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=100)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
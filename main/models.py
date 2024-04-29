from django.db import models


class User(models.Model):
    name = models.CharField("Имя пользователя", max_length=50)
    email = models.EmailField("Почта", unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField("Название фильма", max_length=50)
    director = models.CharField("Режиссер", max_length=50)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name

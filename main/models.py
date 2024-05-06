from django.db import models


class User(models.Model):
    POSITION = (
        ('User', 'Пользователь'),
        ('Worker', 'Сотрудник'),
        ('Admin', 'Админ')
    )

    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    patronynic = models.CharField('Отчество', max_length=100, blank=True)
    email = models.EmailField('Электронная почта', unique=True)
    phone = models.CharField('Телефон', max_length=20, blank=True, null=True, unique=True)
    date_birth = models.DateField('День рождения')
    position = models.CharField('Доступ', max_length=100, choices=POSITION, default='User')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Film(models.Model):
    GENRE = (
        ('Fiction', 'Фантастика'),
        ('Thriller', 'Триллер'),
        ('Roman', 'Роман'),
        ('Detective', 'Детектив'),
        ('Comedy', 'Комендия')
    )

    name = models.CharField("Название фильма", max_length=50)
    director = models.CharField("Режиссер", max_length=50)
    description = models.TextField('Описание', blank=True)
    genre = models.CharField('Жанр', max_length=100, choices=GENRE, default='Comedy')
    public_date = models.DateField('Дата выпуска', blank=True, null=True)
    revenue = models.DecimalField('Выручка', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name

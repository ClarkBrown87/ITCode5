from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.test import APIClient
from main import models


class Test(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.genre = models.Genre.objects.create(name="Фэнтези")
        self.film = models.Film.objects.create(
            name="Титаник",
            director="Джеймс Кэмерон",
            description="Лалалала",
            genre=self.genre,
            public_date='2002-12-12',
            revenue=1200,
            photo=SimpleUploadedFile("media/images.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_list(self):
        response = self.client.get('/films/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(f'/films/{self.film.id}/')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            "name": "Новый фильм",
            "director": "Новый режиссер",
            "description": "Описание нового фильма",
            "genre": self.genre.id,
            "public_date": "2002-10-24",
            "revenue": 1000,
        }
        response = self.client.post('/films/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        new_data = {
            "name": "Трокса",
            "director": "Дэээнис",
            "description": "Качалка",
            "genre": self.genre.id,
            "public_date": "2024-10-24",
            "revenue": 100,
        }

        response = self.client.put(f'/films/{self.film.id}/', data=new_data)

        self.assertEqual(response.status_code, 200)

    def test_partial_update(self):
        partial_new_data = {
            'description': "Обновленное описание"
        }

        response = self.client.patch(f'/films/{self.film.id}/', data=partial_new_data)

        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete(f'/films/{self.film.id}/')
        self.assertEqual(response.status_code, 204)

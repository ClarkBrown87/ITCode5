from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from main import models


class Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.genre = models.Genre.objects.create(name="Фэнтези")
        self.book = models.Film.objects.create(
            name="Титаник",
            director="Джеймс Кэмерон",
            description="Лалалала",
            genre=self.genre,
            public_date='2002-12-12',
            revenue=1200,
            photo=SimpleUploadedFile("media/images.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_index(self):
        response = self.client.get('/index/')
        self.assertEquals(response.status_code, 200)


    def test_genre(self):
        response = self.client.get(f'/genre/{self.genre.id}/')
        self.assertEquals(response.status_code, 200)


    def test_book_detail(self):
        response = self.client.get(f'/film/{self.book.id}/')
        self.assertEquals(response.status_code, 200)
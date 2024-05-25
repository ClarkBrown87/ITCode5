from rest_framework import serializers

from main import models


class Film(serializers.ModelSerializer):
    class Meta:
        model = models.Film
        fields = '__all__'

from django.contrib import admin
from main import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Film)
admin.site.register(models.Genre)
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    year = models.IntegerField()
    genre = models.ManyToManyField(
        'Genre',
        related_name='genre'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category', null=True)

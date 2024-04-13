
# Django
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Album(models.Model):
    title = models.CharField(max_length=255)


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")


class Artist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, related_name="artists")
    albums = models.ManyToManyField(Album, related_name="artists")


# Django
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Album(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self) -> str:
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, related_name="artists")
    albums = models.ManyToManyField(Album, related_name="artists")

    def __str__(self) -> str:
        return self.name

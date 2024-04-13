""" Admin view """

# Django
from django.contrib import admin

# Models
from music.models import Song, Album, Artist


admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)

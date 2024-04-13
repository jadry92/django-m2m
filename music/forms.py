""" Forms for the application """

# django
from django import forms

# models
from music.models import Song, Album


class ArtistForm(forms.Form):
    """ Artist form """
    name = forms.CharField(max_length=50)
    songs = forms.ModelMultipleChoiceField(queryset=Song.objects.all())
    albums = forms.ModelMultipleChoiceField(queryset=Album.objects.all())


""" Forms for the application """

# django
from django import forms

# models
from music.models import Song, Album, Artist


class ArtistForm(forms.ModelForm):
    """ Artist form """
    name = forms.CharField(max_length=50)
    songs = forms.ModelMultipleChoiceField(queryset=Song.objects.all(), widget=forms.CheckboxSelectMultiple)
    albums = forms.ModelMultipleChoiceField(queryset=Album.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Artist
        fields = ["name", "songs", "albums"]

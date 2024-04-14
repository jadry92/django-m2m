""" Song Views """

# Django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Local
from music.models import Song


class SongListView(ListView):
    """ List view for songs. """
    model = Song
    context_object_name = "songs"
    template_name = "music/song/list.html"


class SongDetailView(DetailView):
    """ Detail view for songs. """
    model = Song
    template_name = "music/song/detail.html"


class SongCreateView(CreateView):
    """ Create view for songs. """
    model = Song
    fields = ["title", "album"]
    template_name = "music/song/create.html"
    success_url = reverse_lazy("music:list_song")



class SongUpdateView(UpdateView):
    """ Update view for songs. """
    model = Song
    fields = ["title", "album", "artist"]
    template_name = "music/song/update.html"
    success_url = reverse_lazy("music:list_song")


class SongDeleteView(DeleteView):
    """ Delete view for songs. """
    model = Song
    template_name = "music/song/delete.html"
    success_url = reverse_lazy("music:list_song")


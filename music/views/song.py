""" Song Views """

# Django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
    fields = ["title", "album", "artist"]
    template_name = "music/song/create.html"


class SongUpdateView(UpdateView):
    """ Update view for songs. """
    model = Song
    fields = ["title", "album", "artist"]
    template_name = "music/song/update.html"


class SongDeleteView(DeleteView):
    """ Delete view for songs. """
    model = Song
    template_name = "music/song/delete.html"


"""Albums Views."""

# Django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Local
from music.models import Album, Song, Artist


class AlbumListView(ListView):
    """ List view for albums. """
    model = Album
    context_object_name = "albums"
    template_name = "music/album/list.html"


class AlbumDetailView(DetailView):
    """ Detail view for albums. """
    model = Album
    template_name = "music/album/detail.html"


class AlbumCreateView(CreateView):
    """ Create view for albums. """
    model = Album
    fields = ["title"]
    template_name = "music/album/create.html"


class AlbumUpdateView(UpdateView):
    """ Update view for albums. """
    model = Album
    fields = ["title"]
    template_name = "music/album/update.html"


class AlbumDeleteView(DeleteView):
    """ Delete view for albums. """
    model = Album
    template_name = "music/album/delete.html"

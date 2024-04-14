""" Artist Views. """

# Django
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Local
from music.models import Artist
from music.forms import ArtistForm


class ArtistListView(ListView):
    """ List view for artists. """
    model = Artist
    context_object_name = "artists"
    template_name = "music/artist/list.html"

class ArtistDetailView(DetailView):
    """ Detail view for artists. """
    model = Artist
    template_name = "music/artist/detail.html"


class ArtistCreateView(CreateView):
    """ Create view for artists. """
    template_name = "music/artist/create.html"
    form_class = ArtistForm
    model = Artist
    success_url = reverse_lazy("music:list_artist")

    def get_queryset(self):
        """ Return the artist queryset. """
        queryset = Artist.objects.all()
        return queryset


class ArtistUpdateView(UpdateView):
    """ Update view for artists. """
    model = Artist
    form_class = ArtistForm
    template_name = "music/artist/update.html"
    success_url = reverse_lazy("music:list_artist")


class ArtistDeleteView(DeleteView):
    """ Delete view for artists. """
    model = Artist
    template_name = "music/artist/delete.html"
    success_url = reverse_lazy("music:list_artist")

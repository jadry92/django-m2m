"""Albums Views."""

# Django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next = self.request.GET.get("next", None)
        if next:
            context["next"] = next

        return context

    def get_success_url(self):
        next = self.request.GET.get("next", None)
        if next:
            return next
        return reverse("music:list_album")

class AlbumUpdateView(UpdateView):
    """ Update view for albums. """
    model = Album
    fields = ["title"]
    template_name = "music/album/update.html"


class AlbumDeleteView(DeleteView):
    """ Delete view for albums. """
    model = Album
    template_name = "music/album/delete.html"

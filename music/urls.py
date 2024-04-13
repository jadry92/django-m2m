""" Urls for the music app """

# Django
from django.urls import path

# Views
from music.views import ArtistListView, ArtistDetailView, ArtistCreateView, ArtistUpdateView, ArtistDeleteView

app_name = "music"

urlpatterns = [
    path("artists/", ArtistListView.as_view(), name="index"),
    path("artist/create/", ArtistCreateView.as_view(), name="create_artist"),
    path("artist/<int:pk>/", ArtistDetailView.as_view(), name="index"),
    path("artist/update/<int:pk>/", ArtistUpdateView.as_view(), name="index"),
    path("artist/delete/<int:pk>/", ArtistDeleteView.as_view(), name="index"),
]

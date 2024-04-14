""" Urls for the music app """

# Django
from django.urls import path

# Views
from music.views import ArtistListView, ArtistDetailView, ArtistCreateView, ArtistUpdateView, ArtistDeleteView
from music.views import AlbumListView, AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView
from music.views import SongListView, SongDetailView, SongCreateView, SongUpdateView, SongDeleteView


app_name = "music"

urlpatterns = [
    # Artist
    path("artists/", ArtistListView.as_view(), name="list_artist"),
    path("artist/create/", ArtistCreateView.as_view(), name="create_artist"),
    path("artist/<int:pk>/", ArtistDetailView.as_view(), name="detail_artist"),
    path("artist/<int:pk>/update/", ArtistUpdateView.as_view(), name="update_artist"),
    path("artist/<int:pk>/delete/", ArtistDeleteView.as_view(), name="delete_artist"),
    # Album
    path("albums/", AlbumListView.as_view(), name="list_album"),
    path("album/create/", AlbumCreateView.as_view(), name="create_album"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="detail_album"),
    path("album/update/<int:pk>/", AlbumUpdateView.as_view(), name="update_album"),
    path("album/delete/<int:pk>/", AlbumDeleteView.as_view(), name="delete_album"),
    # Song
    path("songs/", SongListView.as_view(), name="list_song"),
    path("song/create/", SongCreateView.as_view(), name="create_song"),
    path("song/<int:pk>/", SongDetailView.as_view(), name="detail_song"),
    path("song/update/<int:pk>/", SongUpdateView.as_view(), name="update_song"),
    path("song/delete/<int:pk>/", SongDeleteView.as_view(), name="delete_song"),
]

from django.urls import path

from .views import SongList, SongDetailView, AddSongRating

urlpatterns = [
    path('songs/', SongList.as_view(), name='song-list'),
    path('songs/<str:title>/', SongDetailView.as_view(), name='song-detail'),
    path('songs/<str:song_id>/rate/', AddSongRating.as_view(), name='add-song-rating'),
]
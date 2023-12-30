from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Song
from .serializers import SongSerializer, RatingSerializer


class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetailView(APIView):
    def get(self, request, title):
        songs = Song.objects.filter(title__iexact=title)
        if songs.exists():
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Song not found"}, status=status.HTTP_404_NOT_FOUND)


class AddSongRating(APIView):
    def post(self, request, song_id):
        song = Song.objects.get(id=song_id)
        serializer = RatingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.update(song, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
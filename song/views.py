
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song
from rest_framework import status

# Create your views here.

class SongList(APIView):
    def get(self, request, format=None):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SongDetail(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):    #updates
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        song = self.get_object(pk)
        song.delete()
        return Response(song, status=status.HTTP_204_NO_CONTENT)


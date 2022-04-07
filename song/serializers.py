from pyexpat import model
from turtle import title
from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'album', 'release_date', 'genre']
from .models import Singer, Songs
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']

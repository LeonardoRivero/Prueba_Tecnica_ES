from rest_framework import serializers
from .models import Camera, FilmCamera


class FilmCameraSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmCamera
        fields = '__all__'
        # fields = ["markFilm", "sensibility", "formatFilm", "camera"]


class CameraSerializer(serializers.ModelSerializer):
    # cameras = FilmCameraSerializer(many=True, read_only=True)
    # este serializador esta sirviendo ok

    class Meta:
        model = Camera
        fields = '__all__'
        # fields = ["mark", "model", "holderFlash", "cameras"]

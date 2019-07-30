from rest_framework import serializers
from .models import Room, Player

class RoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude=("id")

class PLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
from rest_framework import serializers
from .models import Room, Player

class RoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
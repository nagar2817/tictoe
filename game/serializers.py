from rest_framework import serializers

from .models import BoardState, Player


class BoardStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardState
        fields = ['id', 'data']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'type', 'email', 'board']
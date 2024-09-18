from rest_framework import serializers
from .models import Player, BoardState

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'email']

class BoardStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardState
        fields = ['id', 'player1', 'player2', 'board', 'current_turn']
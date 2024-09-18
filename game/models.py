from django.contrib.postgres.fields import ArrayField
from django.db import models


class BoardState(models.Model):
    data = ArrayField(models.CharField(max_length=1, default='_'), size=9)
    active_player = models.ForeignKey('Player', null=True, on_delete=models.CASCADE)

class Player(models.Model):
    TYPE_CHOICES = [
        ('X', 'X'),
        ('O', 'O'),
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    email = models.EmailField()
    board = models.ForeignKey(BoardState, on_delete=models.CASCADE)
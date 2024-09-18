from django.db import models

class Player(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class BoardState(models.Model):
    player1 = models.ForeignKey(Player, related_name='player1_games', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2_games', on_delete=models.CASCADE)
    board = models.CharField(max_length=9, default='         ')  # 9 spaces for a 3x3 board
    current_turn = models.ForeignKey(Player, related_name='current_turn_games', on_delete=models.CASCADE)

    def __str__(self):
        return f"Game between {self.player1.email} and {self.player2.email}"
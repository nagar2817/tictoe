import re
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BoardState, Player
from .serializers import BoardStateSerializer
from .utils import check_winner, validMove
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render

class MyGameUI(APIView):
      renderer_classes = [TemplateHTMLRenderer]
      template_name = 'index.html'

      def get(self, request):
          return Response()
    
class CreateGameView(APIView):
    def post(self, request, format=None):
        board_state = BoardState.objects.create(data=["_"] * 9)

        # Create player 1
        player1_data = request.data.get('player1')
        player1 = Player.objects.create(type='X', email=player1_data['email'], board=board_state)

        # Create player 2
        player2_data = request.data.get('player2')
        player2 = Player.objects.create(type='O', email=player2_data['email'], board=board_state)

        return Response({'board_id': board_state.id, 'player1_id': player1.id, 'player2_id': player2.id}, status=status.HTTP_201_CREATED)

class UpdateBoardView(APIView):
    def post(self, request):
        i = request.data.get('i')
        j = request.data.get('j')
        user = request.data.get('user')
        board_id = request.data.get('board_id')

        try:
            board = BoardState.objects.get(id=board_id)
            player = Player.objects.get(id=user)
        except (BoardState.DoesNotExist, Player.DoesNotExist):
            return Response({"error": "Invalid board or player ID"}, status=status.HTTP_404_NOT_FOUND)

        if not validMove(i,j, board):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        index = i * 3 + j
        if board.data[index] != '_':
            return Response({"error": "Position already taken"}, status=status.HTTP_400_BAD_REQUEST)

        if board.active_player == player:
            return Response({"error":"you're not allowed!!"}, status=status.HTTP_400_BAD_REQUEST)
            
        board.data[index] = player.type
        board.active_player = player
        board.save()

        if check_winner(board.data, player.type):
            return Response({"message": "Player {} won!".format(player.type),
                            "data":BoardStateSerializer(board).data }, status=status.HTTP_200_OK)

        if '_' not in board.data:
            return Response({"message": "Draw!"}, status=status.HTTP_200_OK)

        return Response(BoardStateSerializer(board).data, status=status.HTTP_200_OK)

class GetLatestStateView(APIView):
    def get(self, request, id):
        try:
            board = BoardState.objects.get(id=id)
        except BoardState.DoesNotExist:
            return Response({"error": "Board not found"}, status=status.HTTP_404_NOT_FOUND)

        active_player = "X" if board.active_player.type == "O" else "O"
        return Response({"board_state": board.data, "active_player": active_player}, status=status.HTTP_200_OK)
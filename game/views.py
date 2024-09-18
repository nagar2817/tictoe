from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Player, BoardState
from .serializers import BoardStateSerializer
from django.shortcuts import render

class RenderHTMLView(APIView):
    def get(self, request):
        return render(request, 'index.html')

class InitializeGameView(APIView):
    def post(self, request):
        player1_email = request.data.get('player1_email')
        player2_email = request.data.get('player2_email')

        if not player1_email or not player2_email:
            return Response({"error": "Both player emails are required"}, status=status.HTTP_400_BAD_REQUEST)

        player1, _ = Player.objects.get_or_create(email=player1_email)
        player2, _ = Player.objects.get_or_create(email=player2_email)

        board_state = BoardState.objects.create(player1=player1, player2=player2, current_turn=player1)

        serializer = BoardStateSerializer(board_state)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UpdateBoardView(APIView):
    def post(self, request):
        board_id = request.data.get('board_id')
        user_id = request.data.get('user_id')
        i = request.data.get('i')
        j = request.data.get('j')

        if not board_id or not user_id or i is None or j is None:
            return Response({"error": "board_id, user_id, i, and j are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            board_state = BoardState.objects.get(id=board_id)
            player = Player.objects.get(id=user_id)
        except (BoardState.DoesNotExist, Player.DoesNotExist):
            return Response({"error": "Invalid board_id or user_id"}, status=status.HTTP_404_NOT_FOUND)

        if board_state.current_turn != player:
            return Response({"error": "Not your turn"}, status=status.HTTP_403_FORBIDDEN)

        index = i * 3 + j
        if board_state.board[index] != ' ':
            return Response({"error": "Invalid move"}, status=status.HTTP_400_BAD_REQUEST)

        new_board = list(board_state.board)
        new_board[index] = 'X' if board_state.current_turn == board_state.player1 else 'O'
        board_state.board = ''.join(new_board)
        board_state.current_turn = board_state.player2 if board_state.current_turn == board_state.player1 else board_state.player1
        board_state.save()

        serializer = BoardStateSerializer(board_state)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetBoardStateView(APIView):
    def get(self, request, board_id):
        try:
            board_state = BoardState.objects.get(id=board_id)
        except BoardState.DoesNotExist:
            return Response({"error": "Board not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BoardStateSerializer(board_state)
        return Response(serializer.data, status=status.HTTP_200_OK)
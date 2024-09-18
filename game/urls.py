from django.urls import path

from .views import CreateGameView, GetLatestStateView, UpdateBoardView, MyGameUI

urlpatterns = [
    path('create_game/', CreateGameView.as_view(), name='create_game'),
    path('update_board/', UpdateBoardView.as_view(), name='update_board'),
    path('get_latest_state/<int:id>/', GetLatestStateView.as_view(), name='get_latest_state'),
    path('', MyGameUI.as_view(), name='game_ui'),
]
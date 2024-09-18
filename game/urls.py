from django.urls import path
from .views import InitializeGameView, RenderHTMLView, UpdateBoardView, GetBoardStateView

urlpatterns = [
    path('initialize-game/', InitializeGameView.as_view(), name='initialize-game'),
    path('update-board/', UpdateBoardView.as_view(), name='update-board'),
    path('get-board-state/<int:board_id>/', GetBoardStateView.as_view(), name='get-board-state'),
    path('', RenderHTMLView.as_view())
]
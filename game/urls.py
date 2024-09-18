from django.urls import path
from .views import InitializeGameView, RenderHTMLView, UpdateBoardView, GetBoardStateView

urlpatterns = [
    path('api/initialize-game/', InitializeGameView.as_view(), name='initialize-game'),
    path('api/update-board/', UpdateBoardView.as_view(), name='update-board'),
    path('api/get-board-state/<int:board_id>/', GetBoardStateView.as_view(), name='get-board-state'),
    path('', RenderHTMLView.as_view())
]
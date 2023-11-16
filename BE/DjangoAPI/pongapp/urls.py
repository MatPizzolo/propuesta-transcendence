from django.urls import path
from . import views

urlpatterns = [
    path('player/', views.getPlayers),
    path('player/<str:pk>', views.getPlayers),
    path('tournament', views.getTournaments),
    path('tournament/<str:pk>', views.getTournaments),
    path('player/add', views.addPlayer),
    path('tournament/add', views.addTournament),
    path('player/update/<str:pk>', views.updatePlayer),
    path('tournament/update/<str:pk>', views.updateTournament),
    path('player/delete/<str:pk>', views.deletePlayer),
    path('tournament/delete/<str:pk>', views.deleteTournament),
]
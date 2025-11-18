from django.urls import path
from . import views

urlpatterns = [
    path('standings/', views.standings, name='standings'),
    path('active-players/', views.active_players, name='active_players'),
    path('active-teams/', views.active_teams, name='active_teams'),
    path('schedule/', views.basic_schedule, name='basic_schedule'),
    path('team-season/', views.team_season, name='team_season'),
    path('player-season/', views.player_season, name='player_season'),
    path('headshots/', views.headshots, name='headshots'),
    path('exportcsv/', views.exportcsv, name='export_csv'),
    ]
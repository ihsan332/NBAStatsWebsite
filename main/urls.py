from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('findplayer/', views.findplayer, name='findplayer'),
    path('findteam/', views.findteam, name='findteam'),
    path('player/<int:player_id>/', views.displayplayer, name='displayplayer'),
    path('team/<int:team_id>/', views.displayteam, name='displayteam'),
    path('standings/', views.standings, name='standings'),
    path('schedule/', views.schedule, name='schedule'),
    path('player/<int:player_id>/delete/', views.delete_player, name='delete_player'),
    path('player/<int:player_id>/update_headshot/', views.update_headshot, name='update_headshot'),
    ]


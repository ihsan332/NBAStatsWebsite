from django.shortcuts import render
from api.models import ActivePlayer, ActiveTeams, Headshot, PlayerSeason, Standings, TeamSeason

# Create your views here.

def home(request):
        if request.user.is_authenticated:
            try:
                userRole = request.user.usertype.role
            except: 
                userRole = 'user'  
        else:
            userRole = 'guest'
        return render(request, 'home.html', {'userRole': userRole})

def findplayer(request):
        if request.user.is_authenticated:
            try:
                userRole = request.user.usertype.role
            except: 
                userRole = 'user' 
        else:
            userRole = 'guest'       
        Players = ActivePlayer.objects.all()
        return render(request, 'findplayer.html',{'Players': Players, 'userRole': userRole})

def findteam(request):
        if request.user.is_authenticated:
            try:
                userRole = request.user.usertype.role
            except: 
                userRole = 'user' 
        else:
            userRole = 'guest'
        Teams = ActiveTeams.objects.all()
        return render(request, 'findteam.html', {'Teams': Teams, 'userRole': userRole})

def displayplayer(request, player_id):
        if request.user.is_authenticated:
            try:
                userRole = request.user.usertype.role
            except: 
                userRole = 'user' 
        else:
            userRole = 'guest'
            player = ActivePlayer.objects.get(player_id=player_id)
            headshot = Headshot.objects.get(player_id=player.player_id)
            season = PlayerSeason.objects.get(player_id=player.player_id)
            return render(request, 'displayplayer.html', {'player':player, 'headshot':headshot, 'season':season, 'userRole': userRole})    

def displayteam(request, team_id):
        if request.user.is_authenticated:
            try:
                userRole = request.user.usertype.role
            except: 
                userRole = 'user' 
        else:
            userRole = 'guest'
        team = ActiveTeams.objects.get(team_id=team_id)
        standing = Standings.objects.get(team_id=team.team_id, season=2024)
        season = TeamSeason.objects.get(team_id=team.team_id, season=2024)
        return render(request, 'displayteam.html', {'team':team, 'season':season, 'standing':standing, 'userRole': userRole})
    
    
    


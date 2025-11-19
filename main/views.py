from django.shortcuts import render
from api.models import ActivePlayer, ActiveTeams, Headshot, PlayerSeason, Standings, TeamSeason, BasicSchedule
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.

def home(request):
        if request.user.is_authenticated:
            try:
                userRole = request.user.usertype.role
            except: 
                userRole = 'guest'  
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
        team = ActiveTeams.objects.filter(team_id=team_id).first()
        standing = Standings.objects.filter(team_id=team.team_id, season=2024).first()  
        season = TeamSeason.objects.filter(team_id=team.team_id, season=2024).first()
        return render(request, 'displayteam.html', {'team':team, 'season':season, 'standing':standing, 'userRole': userRole})
    
    
def standings(request):
        if request.user.is_authenticated:
            try:
                userRole = request.user.usertype.role
            except: 
                userRole = 'user' 
        else:
            userRole = 'guest'
        standings = Standings.objects.all().order_by('-wins')
        return render(request, 'standings.html', {'standing':standings, 'userRole': userRole})


def schedule(request):
        if request.user.is_authenticated:
            try:
                userRole = request.user.usertype.role
            except: 
                userRole = 'user' 
        else:
            userRole = 'guest'

        schedule = BasicSchedule.objects.all().order_by('date_time')
        schedule_data = []
        for game in schedule:
                away_team = ActiveTeams.objects.get(team_id=game.away_team_id)
                home_team = ActiveTeams.objects.get(team_id=game.home_team_id)
                schedule_data.append({'game': game, 'away_team': away_team, 'home_team': home_team})

        return render(request, 'schedule.html', {'schedule_data': schedule_data, 'userRole': userRole})


def delete_player(request, player_id):
    if request.method == 'DELETE':
        player = ActivePlayer.objects.get(player_id=player_id)
        player.delete()
        return JsonResponse({'status': 'deleted'})



def update_headshot(request, player_id):
    if request.method == 'POST':
        link = json.loads(request.body)
        new_headshot_url = link.get('headshot')
        headshot = Headshot.objects.get(player_id=player_id)
        headshot.headshot = new_headshot_url
        headshot.save()
        return JsonResponse({'status': 'updated'})

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ActivePlayer, ActiveTeams, BasicSchedule, Headshot, PlayerSeason, Standings, TeamSeason
import requests
import csv

# Create your views here.

def standingsimport(request):
    api_key = "https://api.sportsdata.io/v3/nba/scores/json/Standings/2024?key=1b9cfb5bc09046c08d3b333f59f1f419"
    
    api = requests.get(api_key).json()

    for standing in api:
        Standings.objects.create(   
            season=standing['Season'],
            team_id=standing['TeamID'],
            key=standing['Key'],
            city=standing['City'],
            fname=standing['Name'],
            conference=standing['Conference'],
            division=standing['Division'],
            wins=standing['Wins'],
            losses=standing['Losses'],
            home_wins=standing['HomeWins'],
            home_losses=standing['HomeLosses'],
            away_wins=standing['AwayWins'],
            away_losses=standing['AwayLosses'],
            streak=standing['Streak'],
            conference_rank=standing['ConferenceRank']    
        )
    return HttpResponse("Standings data imported!")

    
def active_players(request):
    api_key = "https://api.sportsdata.io/v3/nba/scores/json/PlayersActiveBasic?key=1b9cfb5bc09046c08d3b333f59f1f419"
    api = requests.get(api_key).json()
    
    for player in api:
        ActivePlayer.objects.create(
            player_id=player['PlayerID'],
            status=player['Status'],
            team_id=player['TeamID'],
            team=player['Team'],
            jersey=player['Jersey'],
            position=player['Position'],
            fname=player['FirstName'],
            lname=player['LastName'],
            birthdate=player['BirthDate'],
            ethnicity=player['BirthCountry'],
            height=player['Height'],
            weight=player['Weight']   
        )
    return HttpResponse("Standings data imported!")

def active_teams(request):
    api_key = "https://api.sportsdata.io/v3/nba/scores/json/teams?key=1b9cfb5bc09046c08d3b333f59f1f419"
    api = requests.get(api_key).json()
    
    for team in api:
        ActiveTeams.objects.create(
            team_id=team['TeamID'],
            key=team['Key'],
            active=team['Active'],
            city=team['City'],
            name=team['Name'],
            stadium_id=team['StadiumID'],
            conference=team['Conference'],
            logo=team['WikipediaLogoUrl'],
            coach=team['HeadCoach']  
        )
    return HttpResponse("Standings data imported!")

def basic_schedule(request):
    api_key = "https://api.sportsdata.io/v3/nba/scores/json/SchedulesBasic/2024?key=1b9cfb5bc09046c08d3b333f59f1f419"
    api = requests.get(api_key).json()
    
    for game in api:
        BasicSchedule.objects.create(
            game_id=game['GameID'],
            season=game['Season'],
            date_time=game['DateTime'],
            away_team=game['AwayTeam'],
            home_team=game['HomeTeam'],
            away_team_id=game['AwayTeamID'],
            home_team_id=game['HomeTeamID'],
            stadium=game['StadiumID'],
            away_team_score=game['AwayTeamScore'] or 0,
            home_team_score=game['HomeTeamScore'] or 0
        )
    return HttpResponse("Standings data imported!")

def team_season(request):
    api_key = "https://api.sportsdata.io/v3/nba/scores/json/TeamSeasonStats/2024?key=1b9cfb5bc09046c08d3b333f59f1f419"
    api = requests.get(api_key).json()
    
    for team in api:
        TeamSeason.objects.create(
            stat_id=team['StatID'],
            team_id=team['TeamID'],
            season=team['Season'],
            teamname=team['Name'],
            team=team['Team'],
            wins=team['Wins'],
            losses=team['Losses'],
            possessions=team['Possessions'],
            totalgames=team['Games'],
            minutes=team['Minutes'],
            fieldgoals=team['FieldGoalsMade'],
            fieldpercent=team['FieldGoalsPercentage'],
            twogoals=team['TwoPointersMade'],
            twopercent=team['TwoPointersPercentage'],
            threegoals=team['ThreePointersMade'],
            threepercent=team['ThreePointersPercentage'],
            freegoals=team['FreeThrowsMade'],
            freepercent=team['FreeThrowsPercentage'],
            rebounds=team['Rebounds'],
            assists=team['Assists'],
            steals=team['Steals'],
            blocks=team['BlockedShots'],
            turnovers=team['Turnovers'],
            points=team['Points']  
        )
    return HttpResponse("Standings data imported!")

def player_season(request):
    api_key = "https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2024?key=1b9cfb5bc09046c08d3b333f59f1f419"
    api = requests.get(api_key).json()
    
    for player in api:
        PlayerSeason.objects.create(
            stat_id=player['StatID'],
            team_id=player['TeamID'],
            player_id=player['PlayerID'],
            season=player['Season'],
            name=player['Name'],
            team=player['Team'],
            position=player['Position'],
            games=player['Games'],
            fieldgoals=player['FieldGoalsMade'],
            fieldpercent=player['FieldGoalsPercentage'],
            twogoals=player['TwoPointersMade'],
            twopercent=player['TwoPointersPercentage'],
            threegoals=player['ThreePointersMade'],
            threepercent=player['ThreePointersPercentage'],
            freegoals=player['FreeThrowsMade'],
            freepercent=player['FreeThrowsPercentage'],
            rebounds=player['Rebounds'],
            assists=player['Assists'],
            steals=player['Steals'],
            blocks=player['BlockedShots'],
            turnovers=player['Turnovers'],
            points=player['Points']
        )
    return HttpResponse("Standings data imported!")

def headshots(request):
    api_key = "https://api.sportsdata.io/v3/nba/headshots/json/Headshots?key=1b9cfb5bc09046c08d3b333f59f1f419"
    api = requests.get(api_key).json()
    
    for player in api:
        Headshot.objects.create(
            player_id=player['PlayerID'],
            name=player['Name'],
            team_id=player['TeamID'] or 0,
            team=player['Team'] or '',
            position=player['Position'] or '',
            headshot=player['PreferredHostedHeadshotUrl'] or ''
        )
    return HttpResponse("Standings data imported!")


def exportcsv(request):
    download = HttpResponse(content_type='text/csv')
    download['Content-Disposition'] = 'attachment; filename="teams.csv"'

    writer = csv.writer(download)
    writer.writerow(['Team ID', 'Key', 'Active', 'City', 'Name', 'Stadium ID', 'Conference', 'Logo URL', 'Coach'])

    for team in ActiveTeams.objects.all():
        writer.writerow([team.team_id, team.key, team.active, team.city, team.name, team.stadium_id, team.conference, team.logo, team.coach])
    return download



    
from django.contrib import admin
from .models import ActivePlayer, ActiveTeams, BasicSchedule, Headshot, PlayerSeason, Standings, TeamSeason

admin.site.register(ActivePlayer)
admin.site.register(ActiveTeams)
admin.site.register(BasicSchedule)
admin.site.register(Headshot)
admin.site.register(PlayerSeason)
admin.site.register(Standings)
admin.site.register(TeamSeason)


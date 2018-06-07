from django.shortcuts import render
from gameplay.models import Game

def home(req):
  my_games = Game.objects.games_for_user(req.user)
  active_games = my_games.active()

  return render(req, "player/home.html",
    {'games': active_games}
  )

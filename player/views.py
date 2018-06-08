from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import InvitationForm
from .models import Invitation
from gameplay.models import Game

@login_required
def home(req):
  my_games = Game.objects.games_for_user(req.user)
  active_games = my_games.active()

  return render(req, "player/home.html",
    {'games': active_games}
  )

@login_required
def new_invitation(req):
  if req.method == "POST":
    invitation = Invitation(from_user=req.user)
    form = InvitationForm(instance=invitation, data=req.POST)
    if form.is_valid():
      form.save()
      return redirect('player_home')
  else:
    form = InvitationForm()

  return render(req, "player/new_invitation_form.html", {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import InvitationForm
from .models import Invitation
from gameplay.models import Game

@login_required()
def home(req):
  my_games = Game.objects.games_for_user(req.user)
  active_games = my_games.active()
  finished_games = my_games.difference(active_games)
  invitations = req.user.invitations_received.all()

  return render(req, "player/home.html", {
    'active_games': active_games,
    'finished_games': finished_games,
    'invitations': invitations,
  })

@login_required()
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

@login_required()
def accept_invitation(req, id):
  invitation = get_object_or_404(Invitation, pk=id)
  if not req.user == invitation.to_user:
    raise PermissionDenied
  if req.method == "POST":
    if "accept" in req.POST:
      game = Game.objects.create(
        first_player=invitation.to_user,
        second_player=invitation.from_user
      )
      return redirect(game)

    invitation.delete()
    return redirect('player_home')
  else:
    return render(req, "player/accept_invitation_form.html",
      {'invitation': invitation}
    )

class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = 'player/signup_form.html'
  success_url = reverse_lazy('player_home')

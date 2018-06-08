from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import Game
from .forms import MoveForm

@login_required()
def game_detail(req, id):
  game = get_object_or_404(Game, pk=id)
  context = {'game': game}
  if game.is_users_move(req.user):
    context['form'] = MoveForm()
  return render(req, "gameplay/game_detail.html", context)

@login_required()
def make_move(req, id):
  game = get_object_or_404(Game, pk = id)
  if not game.is_users_move(req.user):
    raise PermissionDenied
  move = game.new_move()
  form = MoveForm(instance=move, data=req.POST)
  if form.is_valid():
    move.save()
    return redirect('gameplay_detail', id)
  else:
    return render(req, 'gameplay/game_detail.html', {'game': game, 'form': form})

class AllGamesList(ListView):
  model = Game

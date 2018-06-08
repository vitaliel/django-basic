from django.shortcuts import render, redirect

def welcome(req):
  if req.user.is_authenticated:
    return redirect('player_home')
  else:
    return render(req, 'tictactoe/welcome.html')

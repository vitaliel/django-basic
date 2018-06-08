from django.shortcuts import render

def welcome(req):
  return render(req, 'tictactoe/welcome.html')

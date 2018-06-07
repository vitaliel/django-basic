from django.http import HttpResponse

def welcome(req):
  return HttpResponse("Hello, World!")

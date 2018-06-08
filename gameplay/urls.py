from django.urls import path

from .views import game_detail

urlpatterns = [
  path('detail/<int:id>', game_detail, name='gameplay_detail')
]

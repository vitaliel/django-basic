from rest_framework import serializers

from .models import Game

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    # fields = ('f1', 'f2')
    fields = '__all__'

from rest_framework import serializers
from App.models import LuisAmigo

class LuisAmigoSerializer (serializers.ModelSerializer):
    class Meta:
        model = LuisAmigo
        fields = ['id', 'atividade', 'status']
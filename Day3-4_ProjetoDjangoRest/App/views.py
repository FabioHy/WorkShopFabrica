from django.shortcuts import render
from rest_framework import viewsets
from App.serializers import LuisAmigoSerializer
from App.models import LuisAmigo


# Create your views here.

class LuisAmigoViewSet(viewsets.ModelViewSet):
    queryset = LuisAmigo.objects.all()
    serializer_class = LuisAmigoSerializer

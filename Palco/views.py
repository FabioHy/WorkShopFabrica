from django.shortcuts import render
from rest_framework import viewsets
from Palco.models import Musico, Instrumento
from Palco.serializers import MusicoSerializer, InstrumentoSerializer


# Create your views here.
    
class MusicoView(viewsets.ModelViewSet):
    queryset = Musico.objects.all()
    serializer_class = MusicoSerializer

class InstrumentoView(viewsets.ModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer


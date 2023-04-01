from django.shortcuts import render
from rest_framework import viewsets
from Palco.models import Musico, Instrument
from Palco.serializers import MusicoSerializer, InstrumentSerializer


# Create your views here.

class MusicoView(viewsets.ModelViewSet):
    queryset = Musico.objects.all()
    serializer_class = MusicoSerializer

class InstrumentSerializer(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer


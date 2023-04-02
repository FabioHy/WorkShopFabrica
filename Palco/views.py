from rest_framework import viewsets, generics, status
from .models import Musico, Instrumento
from .serializers import MusicoSerializer, InstrumentoSerializer

from rest_framework.response import Response


# Create your views here.
    
class MusicoView(viewsets.ModelViewSet):
    queryset = Musico.objects.all()
    serializer_class = MusicoSerializer

class InstrumentoView(viewsets.ModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer






from rest_framework import generics
from .models import Musico, Instrumento
from .serializers import MusicoSerializer, InstrumentoSerializer



# Create your views here.
    
class MusicoView(generics.ListCreateAPIView):
    serializer_class = MusicoSerializer
    queryset = Musico.objects.all()

class MusicoEditar(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicoSerializer
    queryset = Musico.objects.all()

class InstrumentoView(generics.ListCreateAPIView):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer

class InstrumentoEditar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer







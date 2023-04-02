from rest_framework import serializers
from Palco.models import Musico, Instrumento

class MusicoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Musico
        fields = ['id', 'nome', 'idade']

class InstrumentoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = ('id', 'modelo', 'quantidade')




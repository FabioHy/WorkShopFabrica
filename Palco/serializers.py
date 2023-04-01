from rest_framework import serializers
from Palco.models import Musico, Instrument

class MusicoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Musico
        fields = ['id', 'nome', 'idade']

class InstrumentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'nome']




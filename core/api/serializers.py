from django.db.models import fields
from rest_framework import serializers
from core import models


class EventoSerializers(serializers.ModelSerializer):
    class Meta:
        models = models.Evento
        fields = '__all__'

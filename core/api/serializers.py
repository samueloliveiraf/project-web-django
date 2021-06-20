
from rest_framework import serializers
from core import models
from django.contrib.auth.models import User


class EventoSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Evento
        fields = "__all__"

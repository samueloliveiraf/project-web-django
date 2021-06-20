from core import models
from rest_framework import viewsets
from core.api import serializers
from core import models
from django.contrib.auth.models import User


class EventoViewsSet(viewsets.ModelViewSet):

    serializer_class = serializers.EventoSerializers
    queryset = models.Evento.objects.all()

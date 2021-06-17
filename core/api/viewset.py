from core import models
from rest_framework import viewsets
from core.api import serializers
from core import models
from rest_framework.permissions import IsAuthenticated


class EventoViewsSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )

    serializer_class = serializers.EventoSerializers
    queryset = models.Evento.objects.all()

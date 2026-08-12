from rest_framework import viewsets

from .models import Site, Device, Interface, Connection
from .serializers import (
    SiteSerializer,
    DeviceSerializer,
    InterfaceSerializer,
    ConnectionSerializer,
)

from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer

class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

class ConnectionTraceView(APIView):
    def get(self, request):
        type = request.query_params.get("type")
        id = request.query_params.get("id")

        if type == "interface":
            connections = Connection.objects.filter(
                Q(start_id=id) | Q(end_id=id)
            )

            serializer = ConnectionSerializer(
                connections,
                many = True,
            )

            return Response({
                "connections": serializer.data
            })
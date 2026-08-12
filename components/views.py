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
        
        elif type == "device":
            interfaces = Interface.objects.filter(
                Q(device_id=id)
            )
            connections = Connection.objects.filter(
                Q(start__device__id=id) | 
                Q(end__device__id=id)
            ).distinct()
                
            connection_serializer = ConnectionSerializer(
                connections,
                many=True,
            )

            interface_serializer = InterfaceSerializer(
                interfaces,
                many=True,
            )

            return Response(
                data={
                    "interfaces": interface_serializer.data,
                    "connections": connection_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        elif type == "site":
            connections = Connection.objects.filter(
                Q(start__device__site__id = id) |
                Q(end__device__site__id = id)
            ).distinct()

            interfaces = Interface.objects.filter(
                Q(device__site__id=id)
            ).distinct()

            devices = Device.objects.filter(
                Q(site_id = id)
            ).distinct()

            connection_serializer = ConnectionSerializer(
                connections,
                many=True,
            )

            interface_serializer = InterfaceSerializer(
                interfaces,
                many=True,
            )

            devices_serializer = DeviceSerializer(
                devices,
                many=True,
            )

            return Response(
                data={
                    "devices": devices_serializer.data,
                    "interfaces": interface_serializer.data,
                    "connections": connection_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
from rest_framework import serializers

from .models import Site, Device, Interface, Connection

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = [
            "id",
            "name",
            "description",
            "status",
        ]

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "id",
            "name",
            "site",
            "serial_number",
        ]

class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = [
            "id",
            "name",
            "device",
            "speed",
            "status",
        ]

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = [
            "id",
            "connection_id",
            "name",
            "status",
            "start",
            "end",
        ]
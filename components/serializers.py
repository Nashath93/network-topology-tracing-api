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

class StartEndSerializer(serializers.Serializer):
    site = serializers.IntegerField(source="device.site_id")
    device = serializers.IntegerField(source="device_id")
    interface = serializers.IntegerField(source="id")

    def validate(self, attrs):
        site_id = attrs["site"]
        device_id = attrs["device"]
        interface_id = attrs["interface"]

        try:
            interface = Interface.objects.get(id=interface_id)
        except Interface.DoesNotExist:
            raise serializers.ValidationError(
                {"interface": "Interface does not exist."}
            )

        attrs["interface_object"] = interface

        return attrs

class ConnectionSerializer(serializers.ModelSerializer):

    start = StartEndSerializer()
    end = StartEndSerializer()

    print("---------")
    print(f"Start: {start}")

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

    def create(self, validated_data):
        start_data = validated_data.pop("start")
        end_data = validated_data.pop("end")

        start_interface = start_data["interface_object"]
        end_interface = end_data["interface_object"]

        return Connection.objects.create(
            start = start_interface,
            end = end_interface,
            **validated_data,
        )
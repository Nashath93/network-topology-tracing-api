from django.db import models
from django.core.exceptions import ValidationError

class Site(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        PLANNED = "planned", "Planned"
        DECOMMISSIONED = "decommissioned", "Decommissioned"

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNED,
    )

    def __str__(self):
        return self.name

class Device(models.Model):

    name = models.CharField(
        max_length=20,
        unique=True,
    )

    """a site can have many devices"""
    site = models.ForeignKey(
        Site,
        on_delete=models.PROTECT, #assumption: do not allow django to delete a site while related devices exist
        related_name="devices",
    )

    serial_number = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return f"{self.name} - {self.serial_number}"

class Interface(models.Model):

    class Status(models.TextChoices):
        UP = "up", "Up"
        DOWN = "down", "Down"
        MAINTENANCE = "maintenance", "Maintenance"

    name = models.CharField(
        max_length=255,
    )

    """a device can have many interfaces"""
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="interfaces",
    )

    speed = models.IntegerField(
        help_text="Mbps",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DOWN,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "device"],
                name="the combination of name and device must be unique",
            )
        ]

    def __str__(self):
        """returns in format: interface_name - device_name"""
        return f"{self.name} - {self.device.name}"

class Connection(models.Model):

    class Status(models.TextChoices):
        CONNECTED = "connected", "Connected"
        DISCONNECTED = "disconnected", "Disconnected"

    connection_id = models.CharField(
        max_length=100,
        unique=True,
    )

    name = models.CharField(
        max_length=255,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CONNECTED,
    )

    """
    connection.start explicitly refer to the interface.
    site, device, interface = (connection.start.device.site, connection.start.device, connection.start)
    """
    start = models.ForeignKey(
        Interface,
        on_delete=models.PROTECT,
        related_name="start_interface",
    )

    end = models.ForeignKey(
        Interface,
        on_delete=models.PROTECT,
        related_name="end_interface",
    )

    def is_point_to_point(self):

        if self.start_id == self.end_id:
            raise ValidationError(
                "A connection must be point-to-point between two Interfaces"
            )
        
        return True

    def __str__(self):
        return self.connection_id












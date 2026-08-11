from django.contrib import admin

from .models import Connection, Device, Interface, Site

admin.site.register(Site)
admin.site.register(Device)
admin.site.register(Interface)
admin.site.register(Connection)

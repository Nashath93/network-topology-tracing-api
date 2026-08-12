from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import (
    SiteViewSet,
    DeviceViewSet,
    InterfaceViewSet,
    ConnectionViewSet,
    ConnectionTraceView,
)

router = DefaultRouter()

router.register("sites", SiteViewSet)
router.register("devices", DeviceViewSet)
router.register("interfaces", InterfaceViewSet)
router.register("connections", ConnectionViewSet)

urlpatterns = [
    path("trace/", ConnectionTraceView.as_view(), name="connection-trace")
]
urlpatterns += router.urls
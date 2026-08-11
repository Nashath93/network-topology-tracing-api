from rest_framework.routers import DefaultRouter

from .views import (
    SiteViewSet,
    DeviceViewSet,
    InterfaceViewSet,
    ConnectionViewSet,
)

router = DefaultRouter()

router.register("sites", SiteViewSet)
router.register("devices", DeviceViewSet)
router.register("interfaces", InterfaceViewSet)
router.register("connections", ConnectionViewSet)

urlpatterns = router.urls
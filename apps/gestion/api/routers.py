from rest_framework.routers import DefaultRouter
from .views.specific_viewsets import *

router = DefaultRouter()


router.register(r'package', PackageViewSet, basename='package')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'shipping', ShippingOrderViewSet, basename='shipping')
router.register(r'user', UserViewSet, basename='user')
router.register(r'trazabilidad', TrazabilidadViewSet, basename='trazabilidad')



urlpatterns = router.urls




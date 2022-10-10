from rest_framework.routers import DefaultRouter
from .views.specific_viewsets import *
from .views.generical_view import *

router = DefaultRouter()


router.register(r'package', PackageViewSet, basename='package')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'shipping', ShippingOrderViewSet, basename='shipping')
router.register(r'user', UserViewSet, basename='user')
router.register(r'trazabilidad', TrazabilidadViewSet, basename='trazabilidad')
router.register(r'departamento',DepartamentoViewSet, basename='departamento'),
router.register(r'municipio', MunicipioViewSet, basename='municipio'),
router.register(r'state', StateViewSet, basename='estado'),
router.register(r'type', TypeViewSet, basename='type'),



urlpatterns = router.urls




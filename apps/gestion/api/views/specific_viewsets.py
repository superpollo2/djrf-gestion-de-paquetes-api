

from ..serializers.specifical_serializers import AddressSerializer,ShippingOrderSerializer,TrazabilidadSerializer,UserSerializer,PackageSerializer

from ..api import GeneralModelViewSet

class PackageViewSet(GeneralModelViewSet):
    serializer_class = PackageSerializer
    
# HTTP methods for address model 
class AddressViewSet(GeneralModelViewSet):
    serializer_class = AddressSerializer


# HTTP methods for shippingOrder model       
class ShippingOrderViewSet(GeneralModelViewSet):
    serializer_class = ShippingOrderSerializer


# HTTP methods for user model  
class UserViewSet(GeneralModelViewSet):
    serializer_class = UserSerializer


# HTTP methods for package model      
class PackageViewSet(GeneralModelViewSet):
    serializer_class = PackageSerializer



# HTTP methods for packege model      
class TrazabilidadViewSet(GeneralModelViewSet):
    serializer_class = TrazabilidadSerializer

    
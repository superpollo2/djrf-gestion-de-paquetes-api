from rest_framework import generics
from rest_framework.response import Response
from ..serializers.specifical_serializers import AddressSerializer,ShippingOrderSerializer,TrazabilidadSerializer,UserSerializer,PackageSerializer
from ...models import Address, ShippingOrder, User, Package,Trazabilidad
from ..api import (
    GeneralListAPIView, GeneralCreateAPIView, GeneralDestroyAPIView,GeneralRetriveAPIView
)

# HTTP methods for address model 
class AddressListAPIView(GeneralListAPIView):
    serializer_class = AddressSerializer
    
class AddressCreateAPIView(GeneralCreateAPIView):
    serializer_class = AddressSerializer
    
class AddressDrestroyAPIView(GeneralDestroyAPIView):
    serializer_class = AddressSerializer

class AddressRetriveAPIView(GeneralRetriveAPIView):
    serializer_class = AddressSerializer
 
# end HTTP methods 

# HTTP methods for shippingOrder model       
class ShippingOrderListAPIView(GeneralListAPIView):
    serializer_class = ShippingOrderSerializer
    
class ShippingOrderCreateAPIView(GeneralCreateAPIView):
    serializer_class = ShippingOrderSerializer
    
# end HTTP methods

# HTTP methods for user model  
class UserListAPIView(GeneralListAPIView):
    serializer_class = UserSerializer
    
class UserCreateAPIView(GeneralCreateAPIView):
    serializer_class = UserSerializer
    
# end HTTP methods

# HTTP methods for package model      
class PackageListAPIView(GeneralListAPIView):
    serializer_class = PackageSerializer

class PackageCreateAPIView(GeneralCreateAPIView):
    serializer_class = PackageSerializer    
    
class PackageDrestroyAPIView(GeneralDestroyAPIView): 
    serializer_class = PackageSerializer

# end HTTP methods

# HTTP methods for packege model      
class TrazabilidadListAPIView(GeneralListAPIView):
    serializer_class = TrazabilidadSerializer

class TrazabilidadCreateAPIView(GeneralCreateAPIView):
    serializer_class = TrazabilidadSerializer 
    
# end HTTP methods
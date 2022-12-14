
from rest_framework import serializers
from .generical_serializers import MunicipioSerializer
from  apps.gestion.models import Trazabilidad,Address,User, Package, ShippingOrder

class PackageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Package
        exclude = ('state','created_date','modified_date', 'deleted_date',)

    def to_representation(self, instance):
        return {
            'id_package': instance.id_package,
            'type': instance.type.type,
            'weight': instance.weight,
            'description': instance.description,
        }
                

class AddressSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = Address
        exclude = ('state','created_date','modified_date', 'deleted_date',)
        
    def to_representation(self, instance):
        return{
            'id_address': instance.id_address,
            'address': instance.address,
            'municipio': instance.municipio.municipio
            
        }   
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ('state','created_date','modified_date', 'deleted_date',)
        
class ShippingOrderSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = ShippingOrder 
        exclude = ('state','created_date','modified_date', 'deleted_date',)
    
    def to_representation(self, instance):
        return {
            'id_shipping': instance.id_shipping,
            'sender': instance.sender.identify,
            'addressee': instance.addressee.identify,
            'price_shipping': instance.price_shipping,
            'address': instance.address.address,
            'date_shipping': instance.date_shipping,
            'package':    instance.package.type.type,
            
                }
        
class TrazabilidadSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = Trazabilidad
        exclude = ('state','created_date','modified_date', 'deleted_date',)

    def to_representation(self, instance):
        return {
            'id_shipping_order': instance.id_shipping_order.id_shipping,
            'date': instance.date,
            'id_state': instance.id_state.state,
        }
        


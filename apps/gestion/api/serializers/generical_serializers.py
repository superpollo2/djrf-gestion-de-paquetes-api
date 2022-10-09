from rest_framework import serializers
from  apps.gestion.models import Departamento,Municipio,Trazabilidad,Address,User,Type, State, Package, ShippingOrder


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        exclude = ('state','created_date','modified_date', 'deleted_date',)

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        exclude = ('state','created_date','modified_date', 'deleted_date',)
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type 
        exclude = ('state','created_date','modified_date', 'deleted_date',)
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State 
        exclude = ('state','created_date','modified_date', 'deleted_date',)
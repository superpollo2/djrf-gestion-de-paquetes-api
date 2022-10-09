from rest_framework import serializers
from  apps.gestion.models import Departamento,Municipio,Trazabilidad,Address,User,Type, State, Package, ShippingOrder


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'
        
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type 
        fields = '__all__'
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State 
        fields = '__all__'
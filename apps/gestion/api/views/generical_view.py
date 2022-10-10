from rest_framework import generics
from ..serializers.generical_serializers import DepartamentoSerializer,MunicipioSerializer, StateSerializer, TypeSerializer
from ...models import Departamento, State, Type, Municipio
from rest_framework.response import Response
from ..api import GeneralViewSet

class DepartamentoViewSet(GeneralViewSet): #heredan de la clase GeneralViewSet ubicada en api.py para ahorrar codigo
    serializer_class = DepartamentoSerializer
    
    
class MunicipioViewSet(GeneralViewSet):
    serializer_class = MunicipioSerializer
    

class StateViewSet(GeneralViewSet):
    serializer_class = StateSerializer
    

class TypeViewSet(GeneralViewSet):
    serializer_class = TypeSerializer
    
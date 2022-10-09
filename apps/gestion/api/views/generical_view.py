from rest_framework import generics
from ..serializers.generical_serializers import DepartamentoSerializer,MunicipioSerializer, StateSerializer, TypeSerializer
from ...models import Departamento, State, Type, Municipio
from rest_framework.response import Response
from ..api import GeneralListAPIView

class DepartamentoListAPIView(GeneralListAPIView): #heredan de la clase GeneralListAPIView ubicada en api.py para ahorrar codigo
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
    
class MunicipioListAPIView(GeneralListAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    

class StateListAPIView(GeneralListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    

class TypeListAPIView(GeneralListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    
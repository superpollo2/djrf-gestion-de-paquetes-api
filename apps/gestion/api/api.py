from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from apps.gestion.models import Departamento, ShippingOrder



class GeneralListAPIView(generics.ListAPIView):
    serializer_class = None 
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class GeneralCreateAPIView(generics.CreateAPIView):
    serializer_class = None
    
    def post (self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Dirección creada con exito'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GeneralDestroyAPIView(generics.DestroyAPIView):
    
    serializer_class = None 
    
    def get_queryset (self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def delete(self, request, pk= None):
        queryset = self.get_queryset() 
        
        object = queryset.filter(pk = pk).first()
        if object :
            object.state = False
            object.save()
            return Response({'message': ' Producto eliminado correctamente'}, status = status.HTTP_200_OK) 
        return Response({'message': 'Error, no existe un registro con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
            
class GeneralRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = None 
    
    def get_queryset(self):
        return  self.get_serializer().Meta.model.objects.filter(state=True)
    
    
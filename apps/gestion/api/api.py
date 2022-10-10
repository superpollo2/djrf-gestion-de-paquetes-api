from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework import viewsets


class GeneralModelViewSet(viewsets.ModelViewSet):
    serializer_class = None 
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(pk = pk).first()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def create(self, request ):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Dirección creada con exito'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        queryset_update = self.get_queryset(pk)
        if queryset_update:
            serializer = self.get_serializer(queryset_update, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        
    def destroy(self, request, pk= None):
        queryset = self.get_queryset() 
        
        object = queryset.filter(pk = pk).first()
        if object :
            object.state = False
            object.save()
            return Response({'message': ' Producto eliminado correctamente'}, status = status.HTTP_200_OK) 
        return Response({'message': 'Error, no existe un registro con esos datos'}, status=status.HTTP_400_BAD_REQUEST)





class GeneralViewSet(viewsets.ModelViewSet):
    serializer_class = None 
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)


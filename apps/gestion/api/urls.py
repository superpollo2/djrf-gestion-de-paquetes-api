from django.urls import path 


from .views.generical_view import *



urlpatterns = [ 
    path('departamento',DepartamentoListAPIView.as_view(), name='departamento'),
    path('municipio', MunicipioListAPIView.as_view(), name='municipio'),
    path('state', StateListAPIView.as_view(), name='estado'),
    path('type', TypeListAPIView.as_view(), name='type'),
               ]
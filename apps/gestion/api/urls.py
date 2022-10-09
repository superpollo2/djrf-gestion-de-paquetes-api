from django.urls import path 

from .views.specific_view import (TrazabilidadCreateAPIView,TrazabilidadListAPIView,AddressListAPIView,AddressDrestroyAPIView, AddressCreateAPIView,ShippingOrderListAPIView,
                                  ShippingOrderCreateAPIView ,UserCreateAPIView,UserListAPIView,PackageListAPIView, PackageCreateAPIView, PackageDrestroyAPIView)
from .views.generical_view import ( DepartamentoListAPIView,MunicipioListAPIView,StateListAPIView, 
                                   TypeListAPIView
                                   )
from rest_framework import routers


urlpatterns = [ 
    path('api/departamento',DepartamentoListAPIView.as_view(), name='departamento'),
    path('api/municipio', MunicipioListAPIView.as_view(), name='municipio'),
    path('api/state', StateListAPIView.as_view(), name='estado'),
    path('api/type', TypeListAPIView.as_view(), name='type'),
    path('address/list', AddressListAPIView.as_view(), name='address_list'),
    path('address/create', AddressCreateAPIView.as_view(), name='address_create'),
    path('address/destroy/<int:pk>', AddressDrestroyAPIView.as_view(), name ='address_destroy'),
    path('shipping/list', ShippingOrderListAPIView.as_view(), name='shipping_list'),
    path('shipping/create', ShippingOrderCreateAPIView.as_view(), name='shipping_create'),
    path('paquete/list', PackageListAPIView.as_view(), name='package_list'), 
    path('paquete/create', PackageCreateAPIView.as_view(), name='package_create'),
    path('paquete/destroy/<int:pk>', PackageDrestroyAPIView.as_view(), name ='package_destroy'),
    
    path('user/list', UserListAPIView.as_view(), name='paquete_list'), 
    path('user/create', UserCreateAPIView.as_view(), name='package_create'),
    path('trazabilidad/list', TrazabilidadListAPIView.as_view(), name='paquete_list'), 
    path('trazabilidad/create', TrazabilidadCreateAPIView.as_view(), name='package_create'),
               ]
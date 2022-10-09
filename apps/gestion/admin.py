from django.contrib import admin
from . models import Departamento,Municipio,Trazabilidad,Address,User,Type, State, Package, ShippingOrder
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',)
   
class DepartamentoAdmin(admin.ModelAdmin):
   exclude = ('created_date','modified_date','deleted_date',) 
    
class MunicipioAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',) 
    
class StateAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',) 

class DepartamentoAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',) 

class UserAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',)
    
class TrazabilidadAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',)
    
class ShippingOrderAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',)

class PackageAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',)

class AddressAdmin(admin.ModelAdmin):
    exclude = ('created_date','modified_date','deleted_date',)
        
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Trazabilidad, TrazabilidadAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(ShippingOrder, ShippingOrderAdmin)
admin.site.register(Address, AddressAdmin)

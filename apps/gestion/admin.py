from django.contrib import admin
from . models import Departamento,Municipio,Trazabilidad,Address,User,Type, State, Package, ShippingOrder
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id_type","type",)
    search_fields = ("id_type",)
    list_filter= ("type",)
    
    
class ShippingOrderList(admin.ModelAdmin):
    list_display = ("id_shipping","sender","addressee", "package",)
    search_fields = ("id_shipping",)
    list_filter= ("package",)
    
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Trazabilidad)
admin.site.register(User)
admin.site.register(Type, TypeAdmin)
admin.site.register(State)
admin.site.register(Package)
admin.site.register(ShippingOrder)
admin.site.register(Address)

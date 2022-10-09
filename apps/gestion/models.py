from email.policy import default
from tabnanny import verbose
from apps.base.models import BaseModel
from django.db import models

from datetime import date
    
class Departamento(BaseModel):
    cod_depa = models.CharField(max_length=10, blank=False, null=False, primary_key=True)
    departament = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return self.departament

class Municipio(BaseModel):
    pos_code = models.CharField(max_length=10, blank=False, null=False, primary_key=True)
    municipio = models.CharField(max_length=50, blank=False, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.municipio   

class Address(BaseModel):
    address = models.CharField(max_length=100, blank=False, null=False, primary_key=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.address  
    
               
class User(BaseModel):
    identify = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    
    
    def __str__(self):
        return self.identify
 
class Type (BaseModel):
    id_type= models.CharField(max_length=4, blank=False, null=False, primary_key=True) 
    price = models.IntegerField(default=0, null=False, blank=False) 
    type = models.CharField(max_length=20, blank=False, null=False) 
    
    def __str__(self):
        return self.type
 
         
class State(BaseModel):
    id_state= models.CharField(max_length=4, blank=False, null=False, primary_key=True) 
    state = models.CharField(max_length=20, blank=False, null=False) 
    
    def __str__(self):
        return self.state
    

    
class Package(BaseModel):
     id_package = models.BigAutoField(primary_key=True)
     type = models.ForeignKey(Type, on_delete = models.CASCADE)
     weight = models.IntegerField(null=False, blank=False)
     description = models.TextField(max_length=200,blank=False, null=False)
      
     def __str__(self):
        return str(self.id_package)

    
class ShippingOrder(BaseModel):
    id_shipping = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete = models.CASCADE,related_name='remitente')
    addressee = models.ForeignKey(User, on_delete = models.CASCADE, related_name='destinatario')
    price_shipping = models.IntegerField(default=0, null=False, blank=False) 
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date_shipping = models.DateField(default=date.today)
    package = models.ForeignKey(Package, on_delete=models.CASCADE) 
    
    
    def __str__(self):
        return str(self.id_shipping)
    
    
class Trazabilidad(BaseModel):
    id_shipping_order = models.ForeignKey(ShippingOrder,on_delete=models.CASCADE)
    date = models.DateTimeField(default= date.today)
    id_state = models.OneToOneField(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_state)
from enum import auto
from django.db import models
from datetime import date 
class BaseModel(models.Model):
       
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de creación', auto_now = False,default= date.today)
    modified_date = models.DateField('Fecha de modificación', auto_now = False, default= date.today)
    deleted_date = models.DateField('Fecha de eliminación', auto_now = False, default= date.today)
    
    
    class Meta:
        abstract = True
        verbose_name = 'modelo base'
        
   
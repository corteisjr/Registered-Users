from django.db import models
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.db.models.fields import CharField

class FullUser(models.Model):
    fullName = models.CharField(max_length=50)
    cpf = CPFField(masked=True)
    age = models.IntegerField()
    address = CharField(max_length=100)
    
    
    def __str__(self):
        return self.fullName
    
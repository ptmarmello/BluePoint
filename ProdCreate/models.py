from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Seguradora(models.Model):
    name = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    num_produtos = models.IntegerField(default=0)
    num_riscos = models.IntegerField(default=0)
    num_contracts = models.IntegerField(default=0)
    products = models.ManyToManyField('Product')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=30)
    product_desc= models.CharField(max_length=2000)
    contract_num= models.IntegerField(default=0)
    sinistro_num= models.IntegerField(default=0)
    access_num=models.IntegerField(default=0)
    #lista_palavraschave=models.IntegerField(default=0)
    gps_location= models.BooleanField(default=False)
    map_structure= models.BooleanField(default=False)
    timer_disposal= models.BooleanField(default=False)
    timer_display = models.IntegerField(default = 0)
    preco_display= models.BooleanField(default=False)
    preco_total = models.IntegerField(default=0)
    belongs_to = models.ForeignKey(Seguradora, related_name='Seguradora',on_delete= models.CASCADE, null="True")
    
    def __str__(self):
        return self.name

class Usuario(models.Model):
    name = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    saldo_num = models.IntegerField(default=0)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return self.name

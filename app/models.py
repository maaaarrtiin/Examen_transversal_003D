from django.db import models
import random

def random_string():
    return str(random.randint(100000000, 999999999))

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    telefono= models.IntegerField(verbose_name='Telefono')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    edad = models.IntegerField(verbose_name='Edad')
    cantidad_mascotas = models.IntegerField(verbose_name='Cantidad de Mascotas')


    def __str__(self):
        return self.rut


class Producto(models.Model):
    idprod = models.CharField(primary_key=True,max_length=10, verbose_name='Id Producto')
    image = models.ImageField(verbose_name="Imagen", upload_to="images")
    nombprod = models.CharField(max_length=50, verbose_name='Nombre producto')
    descripcion_prod= models.CharField(max_length=1000, verbose_name='Descripcion del producto')
    stock = models.IntegerField(verbose_name='Stock del producto')


    def __str__(self):
        return self.idprod



class Compra(models.Model):
    idorden = models.CharField(verbose_name="Numero de orden", default = random_string ,primary_key=True, max_length=10)
    nomb = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    correo= models.CharField(max_length=50, verbose_name='Correo')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    nombre_del_producto = models.CharField(max_length=50, verbose_name='Nombre del producto')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    seguimiento = models.CharField(default = "En preparación",max_length=50, verbose_name='Seguimiento',blank=True)


    def __str__(self):
        return self.idorden
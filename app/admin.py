from django.contrib import admin
from .models import Cliente,Producto,Compra
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Compra)
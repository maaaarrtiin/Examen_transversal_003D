from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente,Producto,Compra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




PROD_CHOICES = [
    ('Correa para gatos', 'Correa para gatos'),
    ('Arenal para gatos', 'Arenal para gatos'),
    ('Correa para perros', 'Correa para perros'),
    ('Torre para gatos', 'Torre para gatos'),
    ('Casa para perros', 'Casa para perros'),
    ('Bandanas', 'Bandanas'),
]


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'telefono', 'correo', 'direccion','edad', 'cantidad_mascotas']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'telefono': 'Telefono', 
            'correo': 'Correo',
            'direccion': 'Direccion',
            'edad': 'Edad',
            'cantidad_mascotas': 'Cantidad de mascotas',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                }
            ), 
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese edad', 
                    'id': 'edad'
                }
            ), 
            'cantidad_mascotas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cantidad de mascotas',
                    'id': 'cantidad_mascotas',
                }
            )

        }




class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['image','idprod', 'nombprod', 'descripcion_prod', 'stock']
        labels ={
            'idprod': 'ID del producto', 
            'nombprod': 'Nombre del producto', 
            'descripcion_prod': 'Descripcion del producto',
            'stock': 'Stock del producto',
        }
        widgets={
            'idprod': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id del producto', 
                    'id': 'idprod'
                }
            ), 
            'nombprod': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el nombre del producto', 
                    'id': 'nombprod'
                }
            ), 
            'descripcion_prod': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la descripcion del producto', 
                    'id': 'descripcion_prod'
                }
            ), 
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el stock del producto', 
                    'id': 'stock'
                }
            )

        }

class CompraForm(forms.ModelForm):
    nombre_del_producto = forms.ChoiceField(choices=PROD_CHOICES)

    class Meta: 
        model= Compra
        fields = ['nomb', 'apellido', 'correo', 'direccion', 'nombre_del_producto','cantidad','seguimiento']
        labels ={ 
            'nomb': 'Nombre', 
            'apellido': 'Apellido',
            'correo': 'Correo',
            'direccion': 'Direccion', 
            'nombre_del_producto': 'Nombre del producto',
            'cantidad': 'Cantidad',
            'seguimiento': 'Seguimiento'
        }
        widgets={
            'nomb': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nomb'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su apellido', 
                    'id': 'apellido'
                }
            ), 
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su correo electronico', 
                    'id': 'correo'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su domicilio', 
                    'id': 'direccion'
                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la cantidad', 
                    'id': 'cantidad'
                }
            ),
            'seguimiento': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el estado', 
                    'id': 'seguimiento'
                }
            ),

        }


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
 
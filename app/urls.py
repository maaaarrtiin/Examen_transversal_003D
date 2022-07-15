from django.conf import settings
from django.conf.urls.static import static

from django.urls import path 
from .views import index, quienessomos, galeria, formulario, apiferiados, registro, apiclientes,mensaje,mostrar,mostrar2,mostrar3,forms_clientes,form_mod_cliente,form_del_cliente,forms_productos,form_mod_producto,form_del_producto,forms_compras,form_mod_compra,form_del_compra

urlpatterns=[
    path('',index, name="index"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('apiferiados/', apiferiados, name="apiferiados"),
    path('apiclientes/', apiclientes, name="apiclientes"),
    path('mensaje/', mensaje, name="mensaje"),
    path('mostrar/', mostrar, name="mostrar"),
    path('mostrar2/', mostrar2, name="mostrar2"),
    path('mostrar3/', mostrar3, name="mostrar3"),
    path('forms_clientes/', forms_clientes, name="forms_clientes"),
    path('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path('forms_productos/', forms_productos, name="forms_productos"),
    path('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
    path('forms_compras/', forms_compras, name="forms_compras"),
    path('form_mod_compra/<id>', form_mod_compra, name="form_mod_compra"),
    path('form_del_compra/<id>', form_del_compra, name="form_del_compra"),    
    path('registro/', registro, name="registro"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
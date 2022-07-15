# Generated by Django 4.0.6 on 2022-07-15 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idorden', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Numero de orden')),
                ('nomb', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('nomb_prod', models.CharField(max_length=50, verbose_name='Nombre del producto')),
                ('seguimiento', models.CharField(default='En preparación', max_length=50, verbose_name='Seguimiento')),
            ],
        ),
    ]
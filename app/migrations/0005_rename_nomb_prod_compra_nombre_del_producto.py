# Generated by Django 4.0.6 on 2022-07-15 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_compra_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='nomb_prod',
            new_name='nombre_del_producto',
        ),
    ]
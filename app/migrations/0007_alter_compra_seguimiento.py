# Generated by Django 4.0.6 on 2022-07-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_compra_seguimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='seguimiento',
            field=models.CharField(blank=True, default='En preparación', max_length=50, verbose_name='Seguimiento'),
        ),
    ]
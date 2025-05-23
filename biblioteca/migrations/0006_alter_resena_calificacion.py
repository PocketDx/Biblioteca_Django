# Generated by Django 5.2 on 2025-04-25 12:29

import biblioteca.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_alter_autor_nombre_alter_libro_resumen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resena',
            name='calificacion',
            field=models.FloatField(validators=[biblioteca.models.validar_calificacion, django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]

# Generated by Django 4.2.22 on 2025-06-10 09:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productmodel_breif_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount_percent',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_unit_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_unit_is_integer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='slug',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Сокращенное именование'),
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_unit_slug_alter_product_last_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='is_integer',
            field=models.BooleanField(default=False, help_text='Например - штука', verbose_name='Целочисленная единица измерения?'),
        ),
    ]
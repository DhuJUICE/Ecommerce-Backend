# Generated by Django 5.0.6 on 2024-06-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0002_alter_product_prodprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prodPrice',
            field=models.FloatField(),
        ),
    ]

# Generated by Django 5.0 on 2024-02-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_products_image_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='images/images'),
        ),
    ]

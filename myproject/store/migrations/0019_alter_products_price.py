# Generated by Django 5.0 on 2024-02-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(default='1000'),
        ),
    ]
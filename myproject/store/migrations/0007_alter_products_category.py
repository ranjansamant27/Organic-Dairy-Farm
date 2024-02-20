# Generated by Django 5.0 on 2024-01-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.IntegerField(choices=[(1, 'dairy & poultry'), (2, 'meat'), (3, 'farm produce')], default=1),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
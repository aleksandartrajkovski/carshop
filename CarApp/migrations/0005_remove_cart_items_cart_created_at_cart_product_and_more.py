# Generated by Django 4.2.2 on 2023-06-19 14:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0004_cart_cartitem_cart_items_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='CarApp.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]

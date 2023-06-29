from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, null=True, blank=True)
    profession = models.CharField(max_length=30, null=True, blank=True)
    skill = models.CharField(max_length=30, null=True, blank=True)
    interest = models.CharField(max_length=30, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=None, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to=None, null=False, blank=False)
    description = models.CharField(max_length=100, null=True, blank=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=6)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cart: {self.user.username} - {self.product.name}"

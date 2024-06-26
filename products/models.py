from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    PAYMENT = models.CharField(
        max_length=50, null=True,
        choices=[
            ('Cash on delivery','Cash on delivery'),
            ('Esewa', 'Esewa')
        ]
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    quantity = models.IntegerField()
    contact_no = models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(10)], max_length=100)
    address = models.CharField(max_length=200)
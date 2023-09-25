from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)

    def __str__(self):
        return self.username
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    stock = models.IntegerField(verbose_name='Stock')
    image = models.ImageField(upload_to='products/', verbose_name='Image')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    
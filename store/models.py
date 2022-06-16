from curses.ascii import US
from os import utime
from tabnanny import verbose
from django.db import models
from pytz import timezone
from mysite import settings
from django.urls import reverse
from django_countries.fields import CountryField



class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

# Create your models here.
class Category(models.Model):
    city = models.CharField(max_length=255, db_index=True)
    country = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural='categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self) -> str:
        return self.city


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='product_creator')
    trip_name = models.CharField(max_length=255)
    trip_city = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=500)
    objects = models.Manager()
    products = ProductManager()
    

    
    class Meta:
        verbose_name_plural='Products'
        ordering = ('-created', )


    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    
    
    def __str__(self) -> str:
        return self.trip_name

    
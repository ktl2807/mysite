from unicodedata import category
from django.contrib import admin
from.models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['city', 'slug']
    prepopulated_fields = {'slug':('city', )}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['trip_name', 'trip_city', 'slug', 'price', 'availability', 'created', 'updated']
    list_filter = ['availability', 'is_active']
    list_editable = ['price', 'availability']
    prepopulated_fields = {'slug':('trip_name', )}
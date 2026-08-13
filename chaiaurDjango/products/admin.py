from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'city', 'total', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
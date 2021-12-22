from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Product, Category

admin.site.register(Category)
admin.site.register(Product)
from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Product

admin.site.register(Product)
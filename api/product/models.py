from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)
    image = models.FileField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.FileField(upload_to='products/', null=True, blank=True);
    rating = models.FloatField(max_length=5.0);
    description = models.TextField(max_length=5000);
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} ({self.price})"


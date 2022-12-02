from django.db import models

class profile(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    
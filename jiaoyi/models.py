from django.db import models

# Create your models here.
class product(models.Model):
    productname = models.CharField(max_length=250)
    productprice = models.CharField(max_length=15)
    productcount = models.CharField(max_length=5)

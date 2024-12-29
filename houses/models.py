from django.db import models

# Create your models here.
# the shape of data
class House(models.Model):
    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField()
    description = models.TextField() 
    address = models.CharField(max_length=140)
    
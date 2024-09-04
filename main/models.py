from django.db import models

# Create your models here.
class Atribut(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField
    description = models.TextField
    quantity = models.IntegerField
    
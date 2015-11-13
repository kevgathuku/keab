from django.db import models

# Create your models here.
from farmer.models import Crop


class Buyer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    name = models.CharField(max_length=200)
    order = models.TextField()
    buyer = models.ForeignKey(Buyer)
    crops = models.ForeignKey(Crop)
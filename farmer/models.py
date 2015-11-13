from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    # The maturity period of this crop
    duration = models.DurationField()
    # max_digits = total digits in the number, including decimals
    price = models.DecimalField(max_digits=7, decimal_places=2)


class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    farm_size = models.CharField(max_length=200)
    crops = models.ManyToManyField(Crop)


class Recommendation(models.Model):
    farmer = models.ForeignKey(Farmer)
    crop = models.ForeignKey(Crop)
    duration_passed = models.DurationField()
    text = models.TextField()


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    crops = models.ManyToManyField(Crop)

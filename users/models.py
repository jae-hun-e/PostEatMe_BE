from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.name


class Mise(models.Model):
    stationname = models.CharField(max_length=100, null=True)
    datatime = models.CharField(max_length=100, null=True)
    so2value = models.CharField(max_length=10, null=True)
    covalue = models.CharField(max_length=10, null=True)
    o3value = models.CharField(max_length=10, null=True)
    no2value = models.CharField(max_length=10, null=True)
    pm10value = models.CharField(max_length=10, null=True)
    khaivalue = models.CharField(max_length=10, null=True)
    khaigrade = models.CharField(max_length=10, null=True)
    so2grade = models.CharField(max_length=10, null=True)
    cograde = models.CharField(max_length=10, null=True)
    o3grade = models.CharField(max_length=10, null=True)
    no2grade = models.CharField(max_length=10, null=True)
    pm10grade = models.CharField(max_length=10, null=True)
    lat = models.FloatField(null=True, blank=True, default=None)
    lng = models.FloatField(null=True, blank=True, default=None)
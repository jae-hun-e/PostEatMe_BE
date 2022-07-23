from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name
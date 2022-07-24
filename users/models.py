from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.name
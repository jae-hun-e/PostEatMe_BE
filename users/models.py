from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=11, null=True)
    num = models.SmallIntegerField(validators=[MinValueValidator(2), MaxValueValidator(10)], default=2, null=True)

    def __str__(self):
        return self.name

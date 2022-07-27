from django.db import models


# Create your models here.
class Memo(models.Model):
    name = models.CharField(max_length=10, null=True)
    Memo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

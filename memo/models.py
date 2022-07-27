from django.db import models


# Create your models here.
class Memo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, null=True)
    Memo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

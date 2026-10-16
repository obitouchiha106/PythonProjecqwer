from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    nomi = models.CharField(max_length=100)
    muallif = models.CharField(max_length=100)
    narxi = models.IntegerField()
    rasm = models.CharField(max_length=500)

    def __str__(self):
        return self.nomi
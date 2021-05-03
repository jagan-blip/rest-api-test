from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    number = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
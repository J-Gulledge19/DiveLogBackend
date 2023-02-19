from django.db import models

# Create your models here.
class Dives(models.Model):
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
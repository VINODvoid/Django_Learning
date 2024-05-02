from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    age = models.IntegerField()
    address =models.TextField()
    

class Car(models.Model):
    name= models.CharField(max_length=20)
    color= models.CharField(max_length=20)
    price= models.IntegerField()
    model= models.CharField(max_length=20)
    year= models.IntegerField()

    def __str__(self) -> str:
        return self.name

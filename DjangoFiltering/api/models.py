from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    name=models.IntegerField()
    city=models.CharField(max_length=50)
    passby=models.CharField(max_length=50)
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    employeeid = models.IntegerField()
    city = models.CharField(max_length=100)

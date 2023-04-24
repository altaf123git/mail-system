from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile=models.IntegerField(max_length=12)
    city=models.CharField(max_length=122)
    
    def __str__(self):
        return self.name
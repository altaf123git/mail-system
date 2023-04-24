from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    field= models.CharField(max_length=500)
    pan= models.FileField(upload_to='static', default="abc", verbose_name="pan")
    
    def __str__(self):
        return self.name
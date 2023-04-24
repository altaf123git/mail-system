from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile= models.CharField(max_length=500)
    pan= models.FileField(upload_to='static', default="abc", verbose_name="pan")
    
    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile= models.CharField(max_length=500)
    desc= models.CharField(max_length=10000)
    
    def __str__(self):
        return self.name
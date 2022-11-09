from django.db import models

# Create your models here.

class Customer(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    passw = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="imagenes", null=True)

    

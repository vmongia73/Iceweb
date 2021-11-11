from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname =models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    email =models.CharField(max_length=30)
    phone =models.CharField(max_length=12)
    city =models.CharField(max_length=20)
    state =models.CharField(max_length=20)
    complaint =models.TextField()

    def __str__(self):
        return self.firstname

class Buy(models.Model):
    firstname =models.CharField(max_length=50)
    icecreamfl =models.CharField(max_length=50)
    quantity =models.CharField(max_length=50)
    phone =models.CharField(max_length=50)
    email =models.CharField(max_length=50)
    city =models.CharField(max_length=50)
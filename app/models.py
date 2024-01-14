from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Form(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username
    

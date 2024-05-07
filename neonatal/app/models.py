from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Reg(AbstractUser):
    
    def __str__(self):
        return self.username
    

class center(models.Model):
    city=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)

    def __str__(self):
        return self.city
    

class chat(models.Model):
    botreply = models.CharField(max_length=200)
    response = models.CharField(max_length=200)  # Assuming there is a response field

    def __str__(self):
        return self.botreply


class appoint(models.Model):
    Doctor = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)  
    Patient = models.CharField(max_length=200) 
    Treatment = models.CharField(max_length=200) 
    Contact = models.CharField(max_length=200) 

    def __str__(self):
        return self.Doctor
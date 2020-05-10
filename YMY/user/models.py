from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address = models.CharField(max_length = 600)
    phone_number = models.IntegerField()
    def __str__(self):
        return str( self.id)
from django.db import models
from datetime import datetime

# Create your models here.



class Categories (models.Model): 
    title = models.CharField(max_length = 200)
    date = models.DateField(datetime.now)
    def __str__(self):
        return self.title

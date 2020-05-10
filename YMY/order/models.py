from django.db import models
from user.models import User
from items.models import Item
from datetime import datetime
# Create your models here.
class Order(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    username = models.CharField(max_length=200) 
    userPhone = models.CharField(max_length=200)
    useraddress = models.CharField(max_length=600)
    email = models.EmailField()
    quantity = models.IntegerField() 
    order_date = models.DateTimeField(default = datetime.now )
    def __str__(self):
        return (str(self.order_date)+' '+self.username)
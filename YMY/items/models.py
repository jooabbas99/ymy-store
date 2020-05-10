from django.db import models
from user.models import User
from categories.models import Categories
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length = 200)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.FloatField()
    descreption = models.TextField(blank = True)
    photo_main = models.ImageField(upload_to='media/' )
    photo_1 = models.ImageField(blank = True ,upload_to='media/')
    photo_2 = models.ImageField(blank = True , upload_to='media/')
    date = models.DateTimeField(blank = True)
    def __str__(self):
        return self.title

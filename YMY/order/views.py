from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import Order
from datetime import datetime
from items.models import Item
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def confirm(request):
    if request.method == 'POST':
        item = request.POST['item']
        username = request.POST['username']
        address = request.POST['address']
        quantity = request.POST['quantity']
        phone = request.POST['phone']
        email = request.POST['email']
        _item = get_object_or_404(Item , pk = item )
        seller = _item.seller
       
        date = datetime.now
        order = Order(item = _item
         , username = username , 
         userPhone = phone , 
         useraddress = address ,
          email = email ,
          quantity = quantity,
        )
        if order.save() :
          send_mail('YMY Store','Thank you for use YMY Store , we receive your request and we will call you soon ,  your items is : '+ _item.title +' , quantity : '+ (quantity) +' , price :' +str(_item.price) + ' , phone'+ phone ,'YMYSTORE2020@gmail.com',[email , seller.email],fail_silently=False)
          messages.success(request,'We Will call you soon ')
        else:
           messages.Failed(request,'Failed to order item ')
        return redirect('items')
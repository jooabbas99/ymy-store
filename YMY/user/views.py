from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
# Create your views here.
from django.contrib.auth import get_user_model

from categories.models import Categories
from items.models import Item
from django.contrib.auth.models import User ,auth
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import Group
from order.models import Order

User = get_user_model()

def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        messages.success(request,'you are now logout')
        return redirect('index')
    else:
        return render(request ,'index.html')#

def login(request):
    #login 
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password = password) 
        if user is not None : 
            auth.login(request,user)
            messages.success(request , 'welcome ')
            print('LOGIN')
            return redirect('index')#
        else:
            messages.error(request,'invalid login data')
            return redirect('login')#
    else:
        return render(request,'account/login.html')#

def register(request):
    if request.method == 'POST' :
        #GET data from form 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        address = request.POST['address']
        # check password
        if password == password2 : 
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'this username already used')
                return redirect('register')#

            else :
                 if User.objects.filter(email=email).exists():
                    messages.error(request,'this email already used')
                    return redirect('register')#
                 else :
                    user = User.objects.create_user(username = username,email = email,password=password,first_name = first_name  , last_name=last_name , phone_number = phone , address = address)
                     #login                     
                    my_group = Group.objects.get(name='user') 
                    my_group.user_set.add(user)
                    user.is_staff = True
                    user.save()
                    #auth.login(request,user=user)
                    messages.success(request ,'you are now registered ')
                    send_mail('YMY Store','Thank you for register in  YMY Store , you can now add items for your account after we accept \n Enjoy with shopping safe  ,  ' ,'YMYSTORE2020@gmail.com',[email ],fail_silently=False)

                    return redirect('login')#
            return redirect('register')#
        else:
            messages.error(request,'password not matched')
            return redirect('register')#
        return redirect('register')#
    else:
        return render(request ,'account/register.html')#



def dashboard(request):
    categories = Categories.objects.all()
    seller = request.user
    orders = Order.objects.order_by('order_date').filter( item__seller = seller )
    context = {
        'categories' : categories,
        'orders' : orders
    }
    return render(request ,'account/dashboard.html',context)

def send_mail_to_delivery(request):
    # order = request.POST['order']
    useraddress = request.POST['useraddress']
    username = request.POST['username']
    userPhone = request.POST['userphone']
    email = request.POST['email']
    order_date = request.POST['order_date']
    itemID = request.POST['itemid']
    item = get_object_or_404(Item, pk = itemID)
    send_mail('YMY Store',' Dear Mr/Mrs '+request.user.last_name+'\n Thank you for use YMY Store \n this delivery information \n  item id : ' + str(item.id) + ' , item name : ' + item.title + ' , item price : ' + str(item.price) +' ,\n for address : '+ str(useraddress)+'  , user name : '+username+' , phone: '+userPhone+' , order Date : '+str(order_date)+' , Email : '+str(email)+'  \n ' ,'YMYSTORE2020@gmail.com',[ request.user.email],fail_silently=False)
    send_mail('YMY Store',' Dear Mr/Mrs '+username+'\n Thank you for use YMY Store \n the request now with delivery  \n for : \n item id : ' + str(item.id) + ' , item name : ' + item.title + ' , item price : ' + str(item.price) +' ,\n your address : '+ str(useraddress)+'  ,  your phone: '+userPhone+' , order Date : '+str(order_date)+'\n ' ,'YMYSTORE2020@gmail.com',[ email],fail_silently=False)
    messages.success(request , 'Sent To Delivery ')
    return redirect('dashboard')

def finish_order(request):
    order = request.POST['order']
    orders = Order.objects.get(id = order).delete()
    messages.success(request , 'The Order Are Finished ')
    return redirect('dashboard')

def delete_item(request):
    if request.method == 'POST':
        item_id = request.POST['id']    
        item = Item.objects.get(id = item_id).delete()   
        messages.success(request , 'The item Are deleted ')
        return redirect('my_items')

def admin_area(request ):   
    return render(request , 'admin/index.html')


def my_items(request) :
    categories = Categories.objects.all()
    items = Item.objects.filter( seller = request.user )
    context = {
        'categories' : categories,
        'items' : items
    }
    return render(request,'account/seller_item.html',context)
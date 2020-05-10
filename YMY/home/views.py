from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from items.models import Item
from categories.models import Categories
# Create your views here.
# here is the response that return the html page 

def index(request):
    # return HttpResponse('<center><h1>Test Page </h1></center>')
    items = Item.objects.order_by('-date')[:3]
    categories = Categories.objects.all()
    context = {
        'items' : items,
        'categories' : categories
    }
    return render(request , 'home/index.html', context)







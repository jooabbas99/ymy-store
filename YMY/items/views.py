from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from .models import Item
from categories.models import Categories

# Create your views here.

def items(request):
    #featch data 
    items = Item.objects.order_by('-date')
    paginator = Paginator(items ,6)
    page = request.GET.get('page')
    page_items = paginator.get_page(page)
    categories = Categories.objects.all()
    context = {
        'items' : page_items,
         'categories' : categories,
         'values' : request.GET 
    }
    return render(request, 'items/item_list.html' , context)

def items_gategory(request , id_cat):
    #featch data 
    items = Item.objects.filter(category = id_cat)
    paginator = Paginator(items ,6)
    page = request.GET.get('page')
    page_items = paginator.get_page(page)
    categories = Categories.objects.all()
    context = {
        'items' : page_items,
         'categories' : categories
    }
    return render(request, 'items/item_list.html' , context)


def search(request ):
    categories = Categories.objects.all()
    items = Item.objects.order_by('-date')
    # item-name = & max_price=
    if 'category' in request.GET : 
        _category = request.GET['category']
        if _category :
            items = items.filter(category = _category)
    
    if 'itemName' in request.GET :
        item_name = request.GET['itemName']
        if item_name :
            items = items.filter(title__icontains=item_name)
    if 'maxPrice'  in request.GET :
        max_price = request.GET['maxPrice']
        if max_price :
            #less than or equal
            items = items.filter( price__lte = max_price)
   
    context = {
        'items' : items,
        'categories' : categories,
        'values' : request.GET 
    }
    return render(request, 'items/item_list.html',context)


def item(request, item_id):
    categories = Categories.objects.all()

    item = get_object_or_404(Item , pk = item_id )
    context = {
        'item' : item,
        'categories' : categories

    }
    return render(request, 'items/item.html', context)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.items, name='items'),
    path('item-id=<int:item_id>', views.item, name='item'),
    path('cat-id=<int:id_cat>', views.items_gategory , name ='catitemlist' ),
    path('search', views.search, name='search')
]
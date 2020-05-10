from django.contrib import admin

# Register your models here.
from .models import Item

class itemAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' , 'category'   ,'price')
    list_filter =('category',)
    search_fields = ('title',)

admin.site.register(Item,itemAdmin)
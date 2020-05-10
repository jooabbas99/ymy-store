from django.contrib import admin

# Register your models here.
from .models import Categories

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title' )
    search_fields = ('title','id')


admin.site.register(Categories,categoryAdmin)
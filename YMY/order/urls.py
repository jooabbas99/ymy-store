from django.urls import path

from . import views
# add path for pages
urlpatterns = [ 
    path('confirm', views.confirm, name='confirm'),
]
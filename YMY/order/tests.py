from django.test import TestCase

# Create your tests here.
from django.urls import path

from . import views
# add path for pages
urlpatterns = [
    # /listings
    path('', views.confirm, name='confirm'),

]
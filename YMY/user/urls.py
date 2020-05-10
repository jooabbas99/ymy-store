
from django.urls import path

from . import views
# add path for pages
urlpatterns = [
    path('login', views.login, name='login'),
    path('admin/', views.admin_area, name='admin_area'),
    path('deleting_item', views.delete_item, name='delete_item'),
    path('my_items', views.my_items, name='my_items'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('send_mail_to_delivery', views.send_mail_to_delivery, name='send_mail_to_delivery'),
    path('finish_order', views.finish_order, name='finish_order'),
    path('logout', views.logout, name='logout')
]

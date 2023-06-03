"""ödevs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appMy.views import *
from appUser.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  index, name="index" ),
    path('about/',  about, name="about" ),
    path('deals/',  deals, name="deals" ),
    path('filter/', filter_deals, name='filter_deals'),
    path('register/', register, name="register" ),
     path('logouth/', logouthuser, name='logouth'),
     path('detail/<id>/', detail, name='detail'),
     path('BasketUser/', BasketUser, name='BasketUser'),
     path('BasketUser/', BasketUser, name='BasketUser'),
     path('BasketUser_delete/<int:id>/', BasketUser_delete, name='BasketUser_delete'),
     path('past_orders/', past_orders, name='past_orders'),
     path('past_orders_delete/<id>/', past_orders_delete, name='past_orders_delete'),
   
     
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

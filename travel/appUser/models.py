from django.db import models
from django.contrib.auth.models import User
from appMy.models import *

# Create your models here.




class Basket(models.Model):
    tuors = models.ForeignKey(Tour, verbose_name=("turadı"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userinfo = models.ForeignKey(Userinfo, verbose_name=("kullanıcı"), on_delete=models.CASCADE, null=True)
    quanity = models.IntegerField(("adet"), null=True)
    total_price = models.IntegerField(("toplam fiyat"), null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_paid = models.BooleanField(default=False, null=True)
 
 
 
class PastOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    tuors = models.ForeignKey(Tour, on_delete=models.CASCADE,null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    # Add any other fields you need for the past order

    def __str__(self):
        return self.user.username
 

   



    
  

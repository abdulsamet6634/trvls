from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Userinfo(models.Model):
    
    tel = models.CharField(("telefon numarası"), max_length=50, null=True)
    email = models.CharField(("email"), max_length=50, null=True)
    password = models.CharField(("şifre"), max_length=50, null=True)
    balance = models.DecimalField(("bakiye"), max_digits=100, decimal_places=2, default=0.00)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
   


    def __str__(self) :
        return self.user.username
  

 

class Continents (models.Model):

    header=models.CharField(("kıta adı"), max_length=50)
    text=models.TextField(("içerik"),max_length=2000)
    img=models.ImageField(("resim"), upload_to="resin",  max_length=500)
    population=models.CharField(("kıta nüfusu"), max_length=50)
    area=models.CharField(("kıta yüz ölçümü"), max_length=50)
    countries_total=models.CharField(("kıtadaki toplam ülke"), max_length=50)
    video=models.TextField(("videos"),max_length=500,null=True)

    def __str__(self):
        return self.header
    
# class countries(models.Model):
#     continents_detail=models.ForeignKey(Continents, verbose_name=("kıta"), on_delete=models.CASCADE,blank=True,null=True)
#     name=models.CharField(("ülke adı"), max_length=50)    
#     text=models.TextField(("ülke içeriği"),max_length=50000)
#     img=models.ImageField(("ülke bayrağı resmi"), upload_to="None",  max_length=500)
#     def __str__(self):
#         return self.name

class countries(models.Model):
    continents = models.ForeignKey(Continents, verbose_name=("kıta"), on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(("ülke adı"), max_length=50)    
    text = models.TextField(("ülke içeriği"), max_length=50000)
    img = models.ImageField(("ülke bayrağı resmi"), upload_to="None", max_length=500)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
   
    citty=models.CharField(("Şehir adı"), max_length=50,blank=True,)
    def __str__(self):
        return self.citty or ""
    
class Tour(models.Model):
    continents = models.ForeignKey(Continents, verbose_name=("kıta"), on_delete=models.CASCADE, blank=True, null=True)
    header=models.CharField(("tur üleksi"), max_length=50)
    text=models.TextField(("içerik"),max_length=5000)
    duration=models.CharField(("tur süresi"), max_length=50,null=True,blank=True)
    price=models.CharField(("fiyat"), max_length=50)
    total_price=models.CharField(("toplam yolcu adeti"), max_length=50,null=True)
    city=models.ManyToManyField(City, verbose_name=("şehirler"),blank=True)
    img=models.ImageField(("ülke bayrağı"), upload_to="None", max_length=500,null=True,blank=True)
    def __str__(self):
        return self.header



  
        

  



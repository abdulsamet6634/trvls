from django.db import models

from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from.models import  *
from decimal import Decimal



# Create your views here.


def register(request):


     
    if request.method=="POST":
        button=request.POST.get("button")
        if button=="Signup":
            username=request.POST.get("name")
            email=request.POST.get("email")
            password1=request.POST.get("password1")
            password2=request.POST.get("password2")
            print(request.POST)
            if password1==password2:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        user=User.objects.create_user(username=username,email=email,password=password1)

                        user.save()
                        userinfo=Userinfo(user=user,email=email,password=password1)
                        userinfo.save()
                        
                        return redirect("register")
                    else:
                        hata="bu email zaten var"
                        context={
                    "hata":hata
                            }
                        return render(request,"user/register.html",context) 
                            
                else:
                    hata="bu kullanıcı zaten var"
                    context={
                   "hata":hata
                          }
                    return render(request,"user/register.html",context)  
                           
            else:
                  hata="şifreler aynı değil"
                  context={
                   "hata":hata
                          }
                  return render(request,"user/register.html",context)        
        elif button=="Login":
            username_login=request.POST.get("name")
            password=request.POST.get("password")
            user=authenticate(username=username_login,password=password)
            print(request.POST)

            if user  is not None:
                login(request,user)
                return redirect("/")
            else:
                 hata="email yada şifre hatalı"
                 context={
                   "hata":hata
              }

                 return render(request,"user/register.html",context)
                






            



    context={}

    return render(request,"user/register.html",context) 

def logouthuser(request):   
     
     logout(request)
     return redirect("/")








from django.db import transaction

@transaction.atomic
def BasketUser(request):
    userinfos = Userinfo.objects.filter(user=request.user)
    bask = Basket.objects.filter(user=request.user)
    total = 0
    for item in bask:
        total += item.total_price

    if request.method == "POST":
        button = request.POST.get("button")
        if button == "edit":
            # Handle edit quantity logic
            for k, v in request.POST.items():
                if k.startswith("quantity"):
                    basket_id = k.split(" ")[1]
                    probask = bask.get(id=basket_id)
                    probask.quanity = int(v)
                    probask.total_price = int(v) * int(probask.tuors.price)
                    probask.save()
            return redirect("BasketUser")
        elif button == "balance":
            # Handle balance update logic
            userinfo = Userinfo.objects.filter(user=request.user).first()
            blnc = userinfo.balance
            balance = Decimal(request.POST.get("balance"))
            balance += blnc
            userinfo.balance = balance
            userinfo.save()
            return redirect("BasketUser")
        elif button == "buynow":
            if not bask:
                hata = "Your cart is empty. Add product for purchase."
                ödemes = "basarisiz"
                context = {
                    "bask": bask,
                    "total": total,
                    "userinfos": userinfos,
                    "hata": hata,
                    "ödemes": ödemes
                }
                return render(request, "basket.html", context)

            totals = total
            userinfo = Userinfo.objects.filter(user=request.user).first()
            blncs = userinfo.balance

            if totals < blncs:
                # Deduct the total amount from the user's balance
                blncs -= totals
                userinfo.balance = blncs
                userinfo.save()

                # Create past orders for each item in the basket
                for item in bask:
                    past_order = PastOrder(
                        user=request.user,
                        tuors=item.tuors,
                        total_price=item.total_price
                    )
                    past_order.save()

                # Delete the items from the basket
                bask.delete()

                # Render the success message and past orders
                ödeme = "Payment made, thank you."
                ödemes = "basarili"
                past_orders = PastOrder.objects.filter(user=request.user)
                context = {
                    "ödeme": ödeme,
                    "ödemes": ödemes,
                    "past_orders": past_orders
                }
                return render(request, "basket.html", context)
            else:
                hata = "Insufficient balance."
                ödemes = "basarisiz"
                context = {
                    "bask": bask,
                    "total": total,
                    "userinfos": userinfos,
                    "hata": hata,
                    "ödemes": ödemes
                }
                return render(request, "basket.html", context)
        
    context = {
        "bask": bask,
        "total": total,
        "userinfos": userinfos,
        
    }
    return render(request, "basket.html", context)
 

def BasketUser_delete(request, id):
    bask = Basket.objects.filter(id=id)
    bask.delete()
    return redirect("BasketUser") 



def past_orders(request):
    past_orders = PastOrder.objects.filter(user=request.user)

    if request.method == "POST":
        button = request.POST.get("button")
        if button == "delete":
            selected_order_id = request.POST.get("order_id")
            selected_order = PastOrder.objects.get(user=request.user, id=selected_order_id)
            selected_order.delete()

    context = {
        "past_orders": past_orders
    }
    return render(request,"user/pastorders.html",context)

def past_orders_delete(request,id):
    past_orders = PastOrder.objects.filter(id=id)
    past_orders.delete()
    return redirect("past_orders")
    

# def BasketUser(request):
    
#     userinfos=Userinfo.objects.filter(user=request.user)
#     bask = Basket.objects.filter(user=request.user)
   

#     total=0
    
#     for i in bask:
#        total += i.total_price 
      


                
#     if request.method == "POST":
#         button = request.POST.get("button")
#         if button == "edit":
#             for k, v in request.POST.items():
#                 if k.startswith("quantity"):
#                     basket_id = k.split(" ")[1]
#                     probask = bask.get(id=basket_id)
#                     probask.quanity = int(v)
#                     probask.total_price = int(v) * int(probask.tuors.price)
#                     probask.save()
#             return redirect("BasketUser")
#         elif button=="balance":
               
                            
#                 userinfo = Userinfo.objects.filter(user=request.user).first()
#                 blnc = userinfo.balance  # Değerin gerçek veritabanı sorgusuyla alınması
#                 balance = Decimal(request.POST.get("balance"))  # Decimal olarak dönüştürme yapılması
#                 balance += blnc  # Doğrudan blnc değişkenini kullanarak işlem yapılması
#                 userinfo.balance = balance
#                 userinfo.save()
        
#                 return redirect("BasketUser")
#         elif  button=="buynow":
#             totals=total
#             userinfo = Userinfo.objects.filter(user=request.user).first()
#             blncs=(userinfo.balance)

#             if totals < blncs:
           
                
#                 for item in bask:
                 
#                     item.delete()

                    
#                 blncs -= totals
#                 userinfo.balance = blncs  # userinfo nesnesinin balance alanını güncelleme
#                 userinfo.save()
#                 bask.update(is_paid=True)
#                 ödeme="ödeme gerçekleşti teşekkür ederiz"
#                 ödemes="basarili"
#                 context={
#                     "ödeme":ödeme,
#                     "ödemes":ödemes,
              
#                 }
#                 return render(request, "basket.html", context)
#             else:
#                 hata = "yetersiz bakiye"
#                 ödemes="basarisiz"    
#                 context = {
#                     "bask": bask,
#                     "total": total,
#                     "userinfos": userinfos,
#                     "hata": hata,
#                     "ödemes":ödemes
                    
#                 }
#                 return render(request, "basket.html", context)
                
            
                



              

            
           
           


#     context={
#         "bask":bask,
#         "total":total,
#         "userinfos":userinfos,
       
       
        
#     }

#     return render(request,"basket.html",context)



# def past_orders(request):
#     past_orders = PastOrder.objects.filter(user=request.user)
#     context = {
#         "past_orders": past_orders
#     }
#     return render(request,"basket.html",context)




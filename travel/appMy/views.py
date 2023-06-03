from django.shortcuts import render,redirect
from.models import *
from appUser.models import *
from django.core.paginator import Paginator

# Create your views here.



def index(request):

    continents=Continents.objects.all()

    paginator = Paginator(continents, 2)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    
    context={
       
        "page_obj":page_obj,
        
    }

    return render( request , "index.html",context)

def about(request):

    context={}

    return render( request , "about.html",context)

def deals(request):

    tours=Tour.objects.all()
    
    # if request.method == "POST":
      
    #     tour_id = request.POST.get("tour_id")
    #     tour = Tour.objects.get(id=tour_id)
    #     basket = Basket(tuors=tour,  )
    #     basket.save()

    if request.method == "POST":
        
        
        tour_id = request.POST.get("tour_id")
        tour = Tour.objects.get(id=tour_id)
        quanty= int(request.POST.get("quantity"))
        total_price=int(tour.price)*int(quanty)
        basket = Basket(user=request.user, tuors=tour,quanity=quanty ,total_price=total_price )
       
        basket.save()

       
       

        
       
        return redirect("deals")
    else:
        tours = Tour.objects.all()
        paginator = Paginator(tours, 4)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "page_obj": page_obj,
        }

    
   
    paginator = Paginator(tours, 4)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        "page_obj":page_obj,
        "tours":tours,
        
    }

    return render( request , "deals.html", context)

def filter_deals(request):
    if request.method == 'POST':
        continent = request.POST.get('Continents')
        price = request.POST.get('Price')
        
        # Filtreleme işlemlerini yapmak için gerekli sorguları oluşturun
        filtered_tours = Tour.objects.filter(continents=continent, price__gt=price)
        
        context = {
            'tours': filtered_tours
        }
        
        return render(request, 'deals.html', context)
    
    
def detail(request,id):
    continents=Continents.objects.get(id=id)
    Countries=countries.objects.filter(continents=continents)
   
    context={
        "continents":continents,
        "Countries":Countries,
        
       
    }

    return render(request,"detail.html",context)
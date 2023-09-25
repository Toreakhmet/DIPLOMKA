from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.http import HttpResponse

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Cart  
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def home(request):
    all_products = Product.objects.filter(stock=2)
    total_price = 0  

    if request.user.is_authenticated: 
        cart, created = Cart.objects.get_or_create(user=request.user)
        total_price = cart.products.aggregate(Sum('price'))['price__sum'] or 0 
    
    if request.method == 'POST':
        if 'product_otpravka' in request.POST:
            product_id = request.POST.get('product_otpravka')
            if product_id:
                try:
                    selected_product = Product.objects.get(id=product_id)
                except Product.DoesNotExist:
                    return HttpResponse("Product with this ID does not exist.")
                except ValueError:
                    return HttpResponse("Invalid product ID.")
                
                cart.products.add(selected_product)
                total_price = cart.products.aggregate(Sum('price'))['price__sum'] or 0  
            else:
                                return HttpResponse('Зарегистриуйтесь')

    
    context = {
        'product': all_products,
        'total_price': total_price,
    }

    return render(request, 'home.html', context)


def profile(request):
    cart = Cart.objects.get(user=request.user)
    products_in_cart = cart.products.all() 
    
    return render(request, 'profile.html', {'products_in_cart': products_in_cart})



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})




def book(request):
    book=Product.objects.filter(stock=4)
    return render(request,'book.html',{'book':book})

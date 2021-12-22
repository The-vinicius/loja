from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart": cart_obj})

def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            print("Mostrar mensagem ao usuário, esse produto acabou!")
            return redirect("cart:home")
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj) # cart_obj.products.remove(product_id)
    else:
        # E o produto se adiciona a instância do campo M2M 
        cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)
    #cart_obj.products.remove(product_obj) # cart_obj.products.remove(product_id)
    #return redirect(product_obj.get_absolute_url())
    # Vamos usar namespace cart
    return redirect("cart:home")
from django.shortcuts import render, get_object_or_404
from .models import Product

# Головна сторінка з усіма продуктами
def look_all_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# Деталі продукту
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})

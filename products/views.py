from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def view_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products-list.html', context)

def view_product_detail(request, product_id):
    """ A view of the product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)
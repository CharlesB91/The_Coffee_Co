from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


# Cart View

def view_cart(request):
    """  """

    return render(request, 'cart/cart.html')


# Add To Cart


def add_to_cart(request, item_id):
    """  """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Added {product.name} to your bag')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


# Edit Cart


def edit_cart(request, item_id):
    """  """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    messages.success(request, f'Changed {product.name} in your bag')
    return redirect(reverse('view_cart'))


# Remove From Cart

def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    product = Product.objects.get(pk=item_id)

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        messages.success(request, f'Removed {product.name} from your bag')
        return redirect(reverse('view_cart'))
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing {product.name} from your bag')
        return HttpResponse(status=500)

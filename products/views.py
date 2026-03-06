import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from .models import (Product, Cart, CartItem, Order, OrderItem,
                     BRANDS_BY_CATEGORY, PRODUCTS_BY_BRAND_CATEGORY, CATEGORY_CHOICES)
from .forms import ProductForm, OrderForm


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_or_create_cart(request):
    if not request.session.session_key:
        request.session.create()
    cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart


def _form_context(form, action, product=None):
    return {
        'form': form, 'action': action, 'product': product,
        'brands_json':   json.dumps(BRANDS_BY_CATEGORY),
        'products_json': json.dumps(PRODUCTS_BY_BRAND_CATEGORY),
    }


# ── AJAX ──────────────────────────────────────────────────────────────────────

def get_brands(request):
    return JsonResponse({'brands': BRANDS_BY_CATEGORY.get(request.GET.get('category', ''), [])})


def get_products_ajax(request):
    key = f"{request.GET.get('category','')}::{request.GET.get('brand','')}"
    return JsonResponse({'products': PRODUCTS_BY_BRAND_CATEGORY.get(key, [])})


# ── Product CRUD ──────────────────────────────────────────────────────────────

def product_list(request):
    query    = request.GET.get('q', '')
    category = request.GET.get('category', '')
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query)|Q(brand__icontains=query)|Q(model_number__icontains=query))
    if category:
        products = products.filter(category=category)
    cat_counts = {c[0]: Product.objects.filter(category=c[0]).count() for c in CATEGORY_CHOICES}
    cart = get_or_create_cart(request)
    return render(request, 'products/product_list.html', {
        'products': products, 'query': query,
        'selected_category': category,
        'categories': CATEGORY_CHOICES,
        'cat_counts': cat_counts,
        'total': Product.objects.count(),
        'cart_count': cart.get_total_items(),
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = get_or_create_cart(request)
    return render(request, 'products/product_detail.html', {
        'product': product,
        'cart_count': cart.get_total_items(),
    })


def product_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ "{form.cleaned_data["name"]}" uploaded successfully!')
            return redirect('product_list')
        messages.error(request, 'Please fix the errors below.')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', _form_context(form, 'Upload'))


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ "{form.cleaned_data["name"]}" updated!')
            return redirect('product_list')
        messages.error(request, 'Please fix the errors below.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', _form_context(form, 'Edit', product))


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        name = str(product)
        product.delete()
        messages.success(request, f'🗑 "{name}" deleted.')
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})


# ── Cart ──────────────────────────────────────────────────────────────────────

def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart    = get_or_create_cart(request)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'🛒 "{product.name}" added to cart!')
    next_url = request.POST.get('next', 'product_list')
    return redirect(next_url)


def cart_remove(request, pk):
    cart = get_or_create_cart(request)
    CartItem.objects.filter(cart=cart, product_id=pk).delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart_view')


def cart_update(request, pk):
    cart = get_or_create_cart(request)
    qty  = int(request.POST.get('quantity', 1))
    item = CartItem.objects.filter(cart=cart, product_id=pk).first()
    if item:
        if qty < 1:
            item.delete()
        else:
            item.quantity = qty
            item.save()
    return redirect('cart_view')


def cart_view(request):
    cart = get_or_create_cart(request)
    return render(request, 'products/cart.html', {
        'cart': cart,
        'cart_count': cart.get_total_items(),
    })


# ── Checkout / Order ──────────────────────────────────────────────────────────

def checkout(request):
    cart = get_or_create_cart(request)
    if cart.get_total_items() == 0:
        messages.error(request, 'Your cart is empty!')
        return redirect('cart_view')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_amount = cart.get_total()
            order.payment = 'Cash on Delivery'
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    name=item.product.name,
                    brand=item.product.brand,
                    price=item.product.price,
                    quantity=item.quantity,
                )
            cart.items.all().delete()
            return redirect('order_success', pk=order.pk)
        messages.error(request, 'Please fix the errors below.')
    else:
        form = OrderForm()

    return render(request, 'products/checkout.html', {
        'cart': cart,
        'form': form,
        'cart_count': cart.get_total_items(),
    })


def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'products/order_success.html', {'order': order})


def buy_now(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart    = get_or_create_cart(request)
    cart.items.all().delete()
    CartItem.objects.create(cart=cart, product=product, quantity=1)
    return redirect('checkout')

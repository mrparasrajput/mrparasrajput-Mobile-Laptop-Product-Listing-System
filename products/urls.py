from django.urls import path
from . import views

urlpatterns = [
    # Product CRUD
    path('',                    views.product_list,       name='product_list'),
    path('product/<int:pk>/',   views.product_detail,     name='product_detail'),
    path('upload/',             views.product_upload,     name='product_upload'),
    path('edit/<int:pk>/',      views.product_edit,       name='product_edit'),
    path('delete/<int:pk>/',    views.product_delete,     name='product_delete'),
    # Cart
    path('cart/',               views.cart_view,          name='cart_view'),
    path('cart/add/<int:pk>/',  views.cart_add,           name='cart_add'),
    path('cart/remove/<int:pk>/',views.cart_remove,       name='cart_remove'),
    path('cart/update/<int:pk>/',views.cart_update,       name='cart_update'),
    # Buy Now & Checkout
    path('buy-now/<int:pk>/',   views.buy_now,            name='buy_now'),
    path('checkout/',           views.checkout,           name='checkout'),
    path('order/<int:pk>/success/', views.order_success,  name='order_success'),
    # AJAX
    path('ajax/brands/',        views.get_brands,         name='get_brands'),
    path('ajax/products/',      views.get_products_ajax,  name='get_products'),
]

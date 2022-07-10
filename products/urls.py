from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='products'),
    path('<product_id>', views.view_product_detail, name='product-detail'),
]
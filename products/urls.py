from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='products'),
    path('<product_id>', views.view_product_detail, name='product-detail'),
    path('add_product/', views.CreateProduct.as_view(), name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
]
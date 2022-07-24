from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='products'),
    path('<product_id>', views.view_product_detail, name='product-detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
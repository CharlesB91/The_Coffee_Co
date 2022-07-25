from .models import Product, Category, Review
from django import forms
from django.forms import ModelForm


# Create Product

class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

# Edit Product

class EditProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

# Rweview Product

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('body',)

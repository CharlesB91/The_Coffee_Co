from .models import Product, Category, Review
from django import forms
from django.forms import ModelForm


# Create Workout Form

class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"


class EditProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('body',)

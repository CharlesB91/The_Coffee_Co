from .models import Testimonial
from django import forms
from django.forms import ModelForm

# Add Testimonial

class AddTestimonalForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = "__all__"
        exclude = ("name", "email")


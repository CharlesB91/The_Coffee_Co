from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Testimonial
from django.db.models.functions import Lower
from .forms import AddTestimonalForm
from django.views import generic, View

# Create your views here.

def index(request):
    """ A view to return the index page """

    testimonials = Testimonial.objects.filter(approved=True).order_by("-created_on")

    testimonial_form = AddTestimonalForm(data=request.POST)
    if testimonial_form.is_valid():
        testimonial_form.instance.email = request.user.email
        testimonial_form.instance.name = request.user.username
        testimonial = testimonial_form.save(commit=False)
        testimonial.save()
        testimonial_form = AddTestimonalForm()
        messages.success(request, 'Thanks ! Your Review Is Pending Approval')
    else:
        testimonial_form = AddTestimonalForm()

    context = {
        "testimonials": testimonials,
        "testimonial_form": testimonial_form,
    }


    return render(request, 'home/index.html', context)
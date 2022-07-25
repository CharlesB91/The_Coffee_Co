from django.contrib import admin
from .models import Testimonial

# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

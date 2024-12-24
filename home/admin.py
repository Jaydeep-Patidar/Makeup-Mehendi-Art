from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Testimonial)
admin.site.register(PortfolioItem)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'date', 'time')
    search_fields = ('name', 'email')
    list_filter = ('service', 'date')

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    list_filter = ('submitted_at',)

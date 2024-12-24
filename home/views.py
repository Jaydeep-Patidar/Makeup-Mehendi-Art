from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import *
# Create your views here.
def home_demo(request):
    return render(request, 'index.html')

# views.py
from django.shortcuts import render
from .models import Service, Portfolio, Testimonial

@login_required
def home_view(request):
    services = Service.objects.all()[:3]  # Top 3 services
    portfolio_items = Portfolio.objects.all()[:6]  # Top 6 portfolio items
    testimonials = Testimonial.objects.all()[:3]  # Top 3 testimonials

    context = {
        'services': services,
        'portfolio_items': portfolio_items,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)



# FOR PORTFOLIO PAGE

from .models import PortfolioItem
@login_required

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    categories = PortfolioItem.CATEGORY_CHOICES
    return render(request, 'portfolio.html', {'portfolio_items': portfolio_items, 'categories': categories})


#FOR SERVICE PAGE
@login_required

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


# FOR BOOKING PAGE 

from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking, Service
from .forms import BookingForm

# Booking Page View
@login_required

def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Send confirmation email to user
            subject_user = "Booking Confirmation"
            message_user = (
                f"Dear {booking.name},\n\n"
                f"Thank you for booking our {booking.service.title} service. "
                f"Here are your details:\n"
                f"Date: {booking.date}\nTime: {booking.time}\n\n"
                "Regards,\nMakeup & Mehendi Team"
            )
            send_mail(subject_user, message_user, settings.DEFAULT_FROM_EMAIL, [booking.email])

            # Notify admin
            subject_admin = "New Booking Notification"
            message_admin = (
                f"New booking:\n\n"
                f"Name: {booking.name}\nService: {booking.service.title}\n"
                f"Date: {booking.date}\nTime: {booking.time}\n"
            )
            send_mail(subject_admin, message_admin, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

            return render(request, 'booking_confirmation.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'booking_page.html', {'form': form})

# Fetch Booking Data for Calendar
@login_required

def booking_data(request):
    bookings = Booking.objects.all()
    events = [
        {
            "title": f"{booking.service.title} - {booking.name}",
            "start": booking.date.strftime("%Y-%m-%d"),
            "allDay": True,
        }
        for booking in bookings
    ]
    return JsonResponse(events, safe=False)



# For Contact page

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactSubmission
@login_required

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save submission to the database
        ContactSubmission.objects.create(name=name, email=email, message=message)

        # Optional: Send an email notification
        send_mail(
            subject=f"Contact Form Submission from {name}",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        return render(request, 'contact_success.html', {'name': name})
    return render(request, 'contact.html')




from django.db import models

# Create your models here.

# FOR HOME PAGE
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - Testimonial"


# FOR PORTFOLIO PAGE

class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('makeup', 'Makeup'),
        ('mehendi', 'Mehendi'),
        ('bridal', 'Bridal'),
        ('party', 'Party'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title


# FOR BOOKING PAGE


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
     

    def __str__(self):
        return f"{self.name} - {self.service.title}, "




# FOR CONTACT PAGE

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"





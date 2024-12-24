"""
URL configuration for MyDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
# from accounts import views
# from home.views import *
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_demo, name='index'),
    path('home/', views.home_view, name='home'),  # Home page
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.service_list, name='service_list'),
    path('contact/', views.contact_view, name='contact'),
    path('booking/', views.booking_page, name='booking_page'),
    path('booking/data/', views.booking_data, name='booking_data'),
    # path('booking/calendar/', views.booking_calendar, name='booking_calendar'),
    # path('login/', views.login_view, name='login'),
    # path('register/', views.register_view, name='register'),

    path('accounts/', include('accounts.accounts_url')),  # Include the accounts app's URLs



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

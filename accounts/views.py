# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout


# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your home page URL name
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login_register.html', {'form_type': 'login'})

# Register View
def register_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            user = User.objects.create_user(username=email, password=password, first_name=name)
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    return render(request, 'login_register.html', {'form_type': 'register'})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logging out



# **************************************************************************************************


# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from .forms import RegisterForm, LoginForm

# # Register View
# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts/login')
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})

# # Login View
# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('dashboard')  # Redirect if already logged in

#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             if user.is_superuser:  # Check if Admin
#                 return redirect('admin_dashboard')
#             else:
#                 return redirect('user_dashboard')
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form})

# # Logout View
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('/login')

# # User Dashboard
# @login_required
# def user_dashboard(request):
#     return render(request, 'accounts/user_dashboard.html')

# # Admin Dashboard
# @login_required
# def admin_dashboard(request):
#     if not request.user.is_superuser:
#         return redirect('user_dashboard')  # Redirect non-admin users
#     return render(request, 'accounts/admin_dashboard.html')

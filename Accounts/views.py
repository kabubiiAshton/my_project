from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.utils import timezone
from django.db.models import Count
import logging
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

logger = logging.getLogger('SmartBallot')
# Create your views here.

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('Accounts:login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = "login.html"

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')
            request.GET.get('next', 'home')
            return redirect('SmartBallot:home')  # later link to Election or SmartBallot dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('SmartBallot:home')

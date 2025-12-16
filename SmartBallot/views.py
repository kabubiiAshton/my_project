from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


# Create your views here.

def register(request):
    return render(request, "register.html")
def login(request):
    return render(request, "login.html")


def service_details(request):
    return render(request, "service-details.html")

def portfolio_details(request):
    return render(request, "portfolio-details.html")
def home(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('SmartBallot:home')

    return render(request, 'index.html', {'form': form})
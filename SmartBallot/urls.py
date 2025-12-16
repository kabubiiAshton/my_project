from django.urls import path
from . import views

app_name = 'SmartBallot'
urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
path('services/', views.service_details, name="services"),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
]

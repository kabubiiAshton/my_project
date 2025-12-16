from django.urls import path
from . import views

urlpatterns = [
    path("plans/", views.plans, name="plans"),
    path("subscribe/<int:plan_id>/", views.subscribe, name="subscribe"),
]

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Plan, Subscription

# Create your views here.

def plans(request):
    plans = Plan.objects.all()
    return render(request, "plans.html", {"plans": plans})

@login_required
def subscribe(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == "POST":
        # For demo: create a Subscription record — in production you'd call Stripe/etc.
        Subscription.objects.create(user=request.user, plan=plan)
        messages.success(request, f"Subscribed to {plan.name} (demo).")
        return redirect("billing:plans")
    return render(request, "subscribe.html", {"plan": plan})
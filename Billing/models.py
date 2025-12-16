from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # simple
    description = models.TextField(blank=True)
    stripe_price_id = models.CharField(max_length=200, blank=True, help_text="If using Stripe")

    def __str__(self):
        return f"{self.name} (${self.price})"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    started_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} -> {self.plan.name}"

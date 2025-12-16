from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('voter', 'Voter'),
        ('officer', 'Election Officer'),
    ]
    id_number = models.IntegerField(default=0)
    is_voter = models.BooleanField(default=True)
    email = models.EmailField(max_length=254, unique=True)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='voter')
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
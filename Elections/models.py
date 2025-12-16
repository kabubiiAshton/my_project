from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

class Election(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'Elections'

    def __str__(self):
        return self.title

    def is_open(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time and self.is_active




class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='candidates')
    position = models.ForeignKey("Position", on_delete=models.CASCADE, related_name="candidates", null=True, blank=True)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="candidates/", blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = 'Elections'

    def __str__(self):
        return f"{self.name} ({self.position.name})"

class Position(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name="positions")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        app_label = 'Elections'

    def __str__(self):
        return f"{self.name} ({self.election.title})"



class Voter(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'Elections'
        unique_together = ('election', 'email')

    def __str__(self):
        return f"{self.full_name} <{self.email}>"


class Vote(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    cast_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'Elections'
        unique_together = ("election", "voter", "position")

    def __str__(self):
        return f"{self.voter} -> {self.candidate}"
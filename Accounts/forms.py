from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from .models import User

User = get_user_model()

# Create your forms here

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'role', 'password1', 'password2', 'id_number']

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords must match.")
        validate_password(p1)
        return cleaned

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email'].split('@')[0]
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
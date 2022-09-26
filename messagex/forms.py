from django import forms
from .models import Messagex
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MessagexCreate(forms.ModelForm):
    class Meta:
        model = Messagex
        fields = ['recipient', 'subject', 'text']

    def clean_subject(self):
        data = self.cleaned_data['subject']
        data += 'haha! '
        return data

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        max_length=256, 
        label="Username:", 
        help_text="Enter a valid email address. You'll need it for password recovery."
        )
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("This Email has been used before, go to 'Forgot Password' to recover your account.")

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
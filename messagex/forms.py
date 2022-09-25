from django import forms
from .models import Messagex
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MessagexCreate(forms.ModelForm):
    class Meta:
        model = Messagex
        fields = ('recipient', 'subject', 'text')

    def clean_subject(self):
        data = self.cleaned_data['subject']
        data += 'haha!'
        # do some stuff
        return data

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
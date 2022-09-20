from django import forms
from .models import Messagex
from cryptography.fernet import Fernet

class MessagexCreate(forms.ModelForm):
    class Meta:
        model = Messagex
        fields = ("subject", "text", "etext", "recipient")

    def clean_subject(self):
        data = self.cleaned_data['subject']
        data += 'haha!'
        # do some stuff
        return data

    def clean_subject(self):
        data = self.cleaned_data['subject']
        data += 'haha!'
        # do some stuff
        
        return data

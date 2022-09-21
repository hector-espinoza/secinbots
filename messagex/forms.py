from django import forms
from .models import Messagex

class MessagexCreate(forms.ModelForm):
    class Meta:
        model = Messagex
        fields = ("recipient", "subject", "text")

    def clean_subject(self):
        data = self.cleaned_data['subject']
        data += 'haha!'
        # do some stuff
        return data

from django import forms
from .models import NewForm, Secure

class NewNewFormForm(forms.ModelForm):
    class Meta:
        model = NewForm
        exclude = []
        widgets = {

        }

class SecureForm(forms.ModelForm):
    class Meta:
        model = Secure
        exclude = []
        widgets = {}

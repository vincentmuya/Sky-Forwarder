from django import forms
from .models import NewForm, Secure

class NewNewFormForm(forms.ModelForm):
    class Meta:
        model = NewForm
        exclude = ['Update2','Update3','Update4','Update5','Update6',]
        widgets = {

        }

class SecureForm(forms.ModelForm):
    class Meta:
        model = Secure
        exclude = []
        widgets = {}

from django import forms
from .models import NewForm

class NewNewFormForm(forms.ModelForm):
    class Meta:
        model = NewForm
        exclude = ['Update2','Update3','Update4','Update5','Update6',]
        widgets = {

        }

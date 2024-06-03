from django import forms
from .models import *


class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class OptForm(forms.ModelForm):
    class Meta:
        model = operator
        fields = ['name', 'line', 'employee_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'line': forms.Select(attrs={'class': 'form-control'}),
            'employee_code': forms.TextInput(attrs={'class': 'form-control'}),

        }

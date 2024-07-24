from django import forms
from .models import *


class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class workinghourform(forms.ModelForm):
    class Meta:
        model = workinghour
        fields = ['name', 'status']
        
class update_combine_form(forms.ModelForm):
    class Meta:
        model = daily_report
        fields = ['combine', 'created_date', 'target', 'remark', 'absant']
        widgets = {
            'combine': forms.NumberInput(attrs={'class': 'form-control'}),
            'target': forms.NumberInput(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
            'created_date': forms.DateInput(attrs={'class': 'form-control'}),

        }


class operatorform(forms.ModelForm):
    class Meta:
        model = operator
        fields = ['name', 'employee_code','burmese', 'point','role','resign']
        

class OptForm(forms.ModelForm):
    class Meta:
        model = operator
        fields = ['name', 'burmese', 'line', 'point', 'employee_code','role']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'burmese': forms.TextInput(attrs={'class': 'form-control'}),
            'line': forms.Select(attrs={'class': 'form-control'}),
            'point': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_code': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),

        }

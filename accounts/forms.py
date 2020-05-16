from django.forms import ModelForm
from django import forms
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

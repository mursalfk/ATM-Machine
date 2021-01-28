from django.forms import ModelForm
from django import forms

# from .models import Order

class WithdrawMoney(forms.Form):
    amount = forms.CharField(
        widget = forms.TextInput(attrs = 
            {
                    'placeholder' : 'Amount'
                }
        )   
    )
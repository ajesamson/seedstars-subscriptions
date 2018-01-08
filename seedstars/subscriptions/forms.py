from django.forms import ModelForm
from django.forms import TextInput
from .models import Subscription


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'email']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'})
        }

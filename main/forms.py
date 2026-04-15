from django import forms
from .models import CakeFlavor, Topping

class FlavorForm(forms.ModelForm):
    class Meta:
        model = CakeFlavor
        fields = ['name']
        labels = {'name': 'Cake Flavor Name'}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name': 'Topping Name'}
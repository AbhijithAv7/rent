from django import forms
from orders.models import *
from dresses.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class DressForm(forms.ModelForm):
    class Meta:
        model = Dress
        fields = ['name', 'category', 'description', 'price_per_day', 'image']
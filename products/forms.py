from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'sku',
            'name',
            'quantity_available',
            'is_active',
        ]
        labels = {
            'sku': 'SKU',
            'name': 'Name',
            'quantity_available': 'Quantity Available',
            'is_active': 'Active',
        }

from django import forms
from .models.seedModels import Product
 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ['name','price','digital','image']

        widgets = {
            'name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'price' : forms.TextInput(attrs = {'class': 'form-control'}),
            'digital' : forms.TextInput(attrs = {'class': 'form-control'}),
            'image' : forms.FileInput(attrs = {'class': 'form-control'}),
        }


   
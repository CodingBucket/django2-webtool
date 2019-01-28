from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]



class RawProductForm(forms.Form):
    title = forms.CharField(
            label='',
            widget=forms.TextInput(
                attrs = {
                    "placeholder": "Your title"
                }
            ) 
        )
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                        attrs = {
                            "placeholder": "Your description",
                            "class": "new-class-name",
                            "rows": 10,
                            "cols": 120
                        }
                    )
                  )
    price = forms.CharField(initial=199.99)
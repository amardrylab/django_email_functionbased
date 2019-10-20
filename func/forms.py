from django import forms

class AddressForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()


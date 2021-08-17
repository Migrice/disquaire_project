from django import forms
#from django.forms.fields import EmailField

class ContactForm(forms.Form):
    name=forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )
    email=forms.EmailField(
        label='Email',
        widget=forms.EmailField(attrs={'class':'form-control'}),
        required=True
    )
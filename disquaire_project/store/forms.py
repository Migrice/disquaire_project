#il permet de generer les formulaires et valider les données dans la vue
from django import forms
#from django.forms.fields import EmailField

class ContactForm(forms.Form):
    name=forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control'}), # utiliser la classe form control qui prend un formulaire
        required=True
    )
    email=forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class':'form-control'}),
        required=True
    )
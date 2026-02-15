from django import forms 
class QRCodeForms(forms.Form):
    resturant_name = forms.CharField(
        max_length=50,
        label='Resturent Name',
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder':'Enter Restaturent name'
        }))
    url = forms.URLField(
        max_length=200,
        label="menu URL",
        widget=forms.URLInput(attrs={
            'class' : 'form-control',
            'placeholder':'Enter Menu URL'
        }))


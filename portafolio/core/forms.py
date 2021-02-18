from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Su nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Su email'}
    ), min_length=3, max_length=100)
    asunto = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Asunto'}
    ), min_length=3, max_length=100)
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Mensaje'}
    ), min_length=10, max_length=1000)
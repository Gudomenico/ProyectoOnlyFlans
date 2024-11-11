from django import forms
from .models import ContactForm
from django.contrib.auth.forms import AuthenticationForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
    
    
    def clean_customer_email(self):
        email = self.cleaned_data.get('customer_email')
        if not email or len(email.strip()) == 0:
            raise forms.ValidationError("El correo electrónico es obligatorio.")
        return email

    def clean_customer_name(self):
        name = self.cleaned_data.get('customer_name')
        if not name or len(name.strip()) == 0:
            raise forms.ValidationError("El nombre del cliente es obligatorio.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message or len(message.strip()) == 0:
            raise forms.ValidationError("El mensaje no puede estar vacío.")
        return message

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



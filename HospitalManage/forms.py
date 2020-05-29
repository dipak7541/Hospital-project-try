from .models import UserRegistration
from django import forms

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model= UserRegistration
        fields= '__all__'
        widgets = {
        'address':forms.Textarea(attrs={'rows':2, 'cols':50}),
        'password': forms.PasswordInput(),
        'conformpass': forms.PasswordInput(),
         }


 



from .models import UserRegistration
from django import forms

class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=32,widgets=forms.TextInput(attrs={'type' : 'password'}))
    conformpassword=forms.CharField(max_length=32,widgets=forms.TextInput(attrs={'type' : 'password'}))  
    class Meta:
        model= UserRegistration
        fields= '__all__'
        widgets = {
        'address':forms.Textarea(attrs={'rows':2, 'cols':50}), 
        }
    def clean_username(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        if UserRegistration.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exits")
        else:
            return username
    def clean_password(self,*args,**kwargs):
        password=self.cleaned_data.get("password")
        conformpassword=self.cleaned_data.get("conformpassword")
        if password==conformpassword:
            return password
        else:
            raise forms.ValidationError("password doesn't match")

 



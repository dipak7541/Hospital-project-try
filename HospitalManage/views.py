from django.shortcuts import render
from django import forms
from .forms import UserRegistrationForm
from .models import UserRegistration

# Create your views here.
def public_user_page(request):
    return render(request,'normal_users/index.html')

def user_registration_details(request):
    form = UserRegistrationForm()
    if request.method=="POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            if (form.cleaned_data['password']==form.cleaned_data['conformpassword']):
                UserRegistration.objects.create(**form.cleaned_data)
            else:
                raise forms.ValidationError("password doesnot match")    
        else:
            print('error')
    context= {
        'form':form
    }
    return render(request,'normal_users/register.html',context)
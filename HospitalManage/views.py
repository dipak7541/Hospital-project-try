from django.shortcuts import render , redirect
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
                UserRegistration.objects.create(**form.cleaned_data)
                return redirect('/')
    context= {
        'form':form
    }
    return render(request,'normal_users/register.html',context)

    def login_user(request):
        loginform=loginForm()
        if request.method=="POST":
            loginform=loginForm(request.POST or None):
            if loginform.is_valid():
                if UserRegistration.objects.filter(username=username).exists():
                    userdata=UserRegistration.objects.filter(username=username)
                    if userdata.password==password
                        firstname=userdata.firstname
                        return redirect('/')
                    else:
                        raise forms.ValidationError("Wrong Password")
                else:
                    raise forms.ValidationError("Username Doesnot Exits") 
                
    return render(request,'normal_users/login.html',firstname)
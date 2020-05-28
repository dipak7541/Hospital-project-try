from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import UserRegistration

# Create your views here.
def public_user_page(request):
    return render(request,'normal_users/index.html')

def user_registration_details(request):
    form = UserRegistrationForm()
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('success')
            return redirect('/')
        else:
            print('error')
    context= {
        'form':form
    }
    return render(request,'normal_users/register.html',context)
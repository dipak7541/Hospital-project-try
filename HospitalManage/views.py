from django.shortcuts import render

# Create your views here.
def public_user_page(request):
    return render(request,'normal_users/index.html')
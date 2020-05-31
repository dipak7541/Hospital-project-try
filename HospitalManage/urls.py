from django.urls import path
from .views import public_user_page, user_registration_details, login_user
from django.views.generic import TemplateView


urlpatterns=[
    path('',public_user_page,name="index"),
    path('register_user',user_registration_details,name="register_user"),
    path('login_user',login_user,name="login_user"),
]

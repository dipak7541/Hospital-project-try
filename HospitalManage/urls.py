from django.urls import path
from .views import public_user_page

urlpatterns=[
    path('',public_user_page,name="index"),
]
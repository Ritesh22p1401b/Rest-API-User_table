from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

app_name='users'

urlpatterns=[
    path('register',Register_user.as_view(),name='register'),
    path('login',obtain_auth_token,name='login'),
    path('allow',UserPermission.as_view(),name='allow'),
    path('details/<int:pk>/',UserDetails.as_view(),name="details"),
]

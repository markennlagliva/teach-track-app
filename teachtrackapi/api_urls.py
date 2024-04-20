
from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.home, name='home'),

    path('sign-up', api_views.signup_user, name='signup_user'),
]
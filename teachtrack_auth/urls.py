
from django.urls import path
from . import views

# Token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token_auth'),

    path('api/login', views.login_and_get_user_token, name='login_and_get_user_token'),
    path('api/logout/', views.logout_user, name='logout_user')
]
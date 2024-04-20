from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# rest_framework
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# Create your views here.
def login_and_get_user_token(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
            return redirect('home')
            # return Response({'token': token.key, 'created': created})
        else:
            messages.error(request, 'Invalid email or password. Please Try again...')
            # return Response({'message': 'Incorrect email or password'}, status=401)
            return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')
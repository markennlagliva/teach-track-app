from django.shortcuts import render
from teachtrack_auth.models import CustomUser, Schedule
from .forms import CustomUserCreateForm

from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
   
    context = {}
    return render(request, 'base.html', context)

def signup_user(request):
    user_form = CustomUserCreateForm(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Successfully Registered!')
    context = {'form': user_form}
    return render(request, 'partially/signup.html', context)
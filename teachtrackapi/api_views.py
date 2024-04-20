from django.shortcuts import render, redirect
from teachtrack_auth.models import CustomUser, Schedule
from .forms import CustomUserCreateForm, ScheduleCreateForm

from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Time
import datetime
from datetime import time

# Create your views here.
def home(request):
    context = {}
    return render(request, 'base.html', context)

def signup_user(request):
    user_form = CustomUserCreateForm(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Successfully Registered!')
            return redirect('home')
    context = {'form': user_form}
    return render(request, 'partially/signup.html', context)

def schedule(request):
    user = User.objects.get(username=request.user.username)
    
   
    current_datetime = datetime.datetime.now()
    date_readable_format = current_datetime.strftime("%B %d, %Y")
    day_of_week = current_datetime.strftime("%A")

    gender_title = 'Sir' if user.gender == 'M' else 'Ma\'am'

    greetings = ''
    if current_datetime.time() < time(12, 0):
        greetings = f'Blessed Morning! {gender_title}'
    elif current_datetime.time() > time(12,0) and current_datetime.time() < time(13, 0):
        greetings = f'Blessed Noon! {gender_title}'
    elif current_datetime.time() >= time(13, 0) and current_datetime.time() <= time(17, 0):
        greetings = f'Blessed Afternoon! {gender_title}' 
    else:
        greetings = f"Have a good night's rest, {gender_title}"
    print(greetings)

    #  QUERY SCHEDULE FOR 2 REAL TIME DATA
    
    context = {'user_info': user, 'greeting': greetings}
    return render(request, 'partially/schedule.html', context)


def add_schedule(request):
    add_form = ScheduleCreateForm(request.POST or None)
    if request.method == 'POST':
        if add_form.is_valid():
            schedule = add_form.save(commit=False)
            schedule.teacherId_id = request.user.id
            schedule.save()
            messages.success(request, 'Schedule added Sucessfully')
            return redirect('add_schedule')
    context = {'add_form': add_form}
    return render(request, 'partially/add_schedule.html', context)

def today_schedule(request):
    pass

def whole_schedule(request):
    pass
    
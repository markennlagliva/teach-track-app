
from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.home, name='home'),
    path('schedule', api_views.schedule, name='schedule'),
    path('add-schedule', api_views.add_schedule, name='add_schedule'),
    path('today-schedule', api_views.today_schedule, name='today_schedule'),
    path('whole-schedule', api_views.whole_schedule, name='whole_schedule'),
    path('sign-up', api_views.signup_user, name='signup_user'),
]
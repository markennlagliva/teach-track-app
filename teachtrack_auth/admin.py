from django.contrib import admin
from .models import CustomUser, Schedule
from django.contrib.auth.admin import UserAdmin


# Custom User Admin
# class CustomUserAdmin(UserAdmin):
#     pass
#     # list_display = ('email_link', user)


# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Schedule)
from django.contrib import admin
from .models import CustomUser, Schedule
from django.contrib.auth.admin import UserAdmin


# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'initial', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'initial', 'gender', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('email', 'initial', 'gender', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'initial')
    ordering = ('email',)


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Schedule)
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

#This manager will handle user creation and other user-related operations:
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
) 

DAY_CHOICES = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)
    
class CustomUser(AbstractUser):
    # username = None #Remove the username filed if not needed
    email = models.EmailField(_('email address'), unique=True, null=True)
    initial = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # Add any additional required fields here

    objects = CustomUserManager()
    def __str__(self) -> str:
        return self.email

class Schedule(models.Model):
    scheduleId = models.AutoField(primary_key=True)
    teacherId = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    subjectName = models.CharField(max_length=100, null=True)
    className = models.CharField(max_length=50, null=True)
    dayofWeek = models.CharField(max_length=20, choices=DAY_CHOICES)
    startTime = models.TimeField()
    endTime = models.TimeField()

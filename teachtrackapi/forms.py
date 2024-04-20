from django import forms
from teachtrack_auth.models import CustomUser, Schedule
from django.contrib.auth.forms import UserCreationForm

# Custom Widget
from .widget import TimePickerInput

class CustomUserCreateForm(UserCreationForm):
    choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    ) 
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email adress'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    initial = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Middle Initial'}))
    gender = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)



    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'initial', 'last_name', 'gender', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['gender'].label_tags = 'text-muted'
        self.fields['gender'].widget.attrs['class'] = 'text-muted'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


    # my_time_field = forms.TimeField(widget=TimePickerInput)

class ScheduleCreateForm(forms.ModelForm):
    day_choices = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    subjectName = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject Name'}))
    className = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Class Name'}))
    dayofWeek = forms.ChoiceField(choices=day_choices, widget=forms.RadioSelect)
    startTime = forms.TimeField(widget=TimePickerInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 8:00 AM'}), label='Start Time')
    endTime = forms.TimeField(widget=TimePickerInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 9:30 PM'}), label='End Time')

    class Meta:
        model = Schedule
        fields = ('subjectName', 'className', 'dayofWeek', 'startTime', 'endTime')

   

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InputLoc

class GisModelForm(forms.ModelForm):
    class Meta:
        model = InputLoc
        fields = '__all__'

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from . import models

class UserSignupform(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class ChangeUser(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')


class InterprofilePic(forms.ModelForm):
    class Meta:
        model =models.UserProfile
        fields = ['prifile_pic']
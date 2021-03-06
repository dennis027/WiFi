
from .models import  *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import *

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user     


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['pic','bio']   


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
       
        fields=['username','email']    

class UserSubscriptionForm(forms.ModelForm):
    class Meta:
        model=Subscriber
       
        fields=['package','location']
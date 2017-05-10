from django import forms
from django.contrib.auth.forms import User
from .models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ProfileForm(forms.ModelForm):

    class Meta:
         model = Profile
         fields = ('idade', 'altura', 'peso')
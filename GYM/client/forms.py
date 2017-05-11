from django import forms
from django.contrib.auth.forms import User
from .models import Profile,Album


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class AlbumForm(forms.ModelForm):

    class Meta:
         model = Profile
         fields = ('idade', 'altura', 'peso')
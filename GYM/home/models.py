from django.db import models
from django import forms

class UserManager(models.Manager):
    def create_user(self,username,password,email,idade,altura,peso):
        new_user = self.create(username=username,password=password,email=email,idade=idade,altura=altura,peso=peso)
        return new_user




class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=35)
    idade = models.IntegerField()
    altura = models.IntegerField()
    peso = models.IntegerField()


    def __str__(self):
        return self.username


    objects = UserManager()

class Profile(models.Model):
    user = models.OneToOneField(User)

    is_premium = models.BooleanField(default=False)
    idade = models.IntegerField(blank=True)
    altura = models.IntegerField(blank=True)
    peso = models.IntegerField(blank=True)

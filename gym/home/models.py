from django.db import models

class UserManager(models.Manager):
    def create_user(self,username,password):
        newuser= self.create(username=username,password=password)
        return newuser




class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    def password(self):
        return self.password

    objects = UserManager()

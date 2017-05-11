from django.contrib.auth.models import Permission, User
from django.db import models
from django.db.models.signals import post_save



class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    idade = models.IntegerField()
    altura = models.IntegerField()
    peso = models.IntegerField()

    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user + ' - ' + self.idade



class Profile(models.Model):
    user = models.ForeignKey(User)
    is_premium = models.BooleanField(default=False)
    idade = models.IntegerField()
    altura = models.IntegerField()
    peso = models.IntegerField()

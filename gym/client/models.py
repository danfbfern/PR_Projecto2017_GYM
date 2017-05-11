from django.contrib.auth.models import Permission, User
from django.db import models
from django.db.models.signals import post_save



class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

#class UserManager(models.Manager):
 #   def create_user(self,username,password,email,idade,altura,peso):
  #      new_user = self.create(username=username,password=password,email=email,idade=idade,altura=altura,peso=peso)
   #     return new_user




#class User(models.Model):
#    username = models.CharField(max_length=20)
#    password = models.CharField(max_length=20)
#    email = models.CharField(max_length=35)
#    idade = models.IntegerField()
#    altura = models.IntegerField()
#    peso = models.IntegerField()


 #   def __str__(self):
  #      return self.username


   # objects = UserManager()

class Profile(models.Model):
    user = models.ForeignKey(User)
    is_premium = models.BooleanField(default=True)
    idade = models.IntegerField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)

#@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


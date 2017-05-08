from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.shortcuts import render
from .models import User
from django.utils.datastructures import MultiValueDictKeyError
from .forms import UserForm

def index(request):

  render(request,'index.html', {'index': index})

  try:
   print('tentei TRY')
   username = request.POST.get('register_username')
   password = request.POST.get('register_password')
   email = request.POST.get('register_email')
   idade = request.POST.get('register_idade')
   altura = request.POST.get('register_altura')
   peso = request.POST.get('register_peso')

  except MultiValueDictKeyError:
   return


  else:
   if username is None:
    print('username in NONE')
    username = request.POST.get('register_username')
    password = request.POST.get('register_password')
    email = request.POST.get('register_email')
    idade = request.POST.get('register_idade')
    altura = request.POST.get('register_altura')
    peso = request.POST.get('register_peso')
    return render(request,'index.html', {'index': index})
   else:
    print('CHEGOU')
    print(username)
    #l = User.objects.create_user(username,password,email,idade,altura,peso)
    l = User.objects.create_user('eu','ola','lfelaf','12','12','12')

    l.save()
    print('olalalalal')

    return render(request,'index.html', {'index': index})















def plans(request):
 return render(request,'plans.html')


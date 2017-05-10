from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib.auth import authenticate, login
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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'client/index.html')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'index.html')
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)















def plans(request):
 return render(request,'plans.html')


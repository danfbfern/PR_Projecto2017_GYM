from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.http import HttpResponse
from .models import Profile
from .forms import UserForm,AlbumForm
from django.utils.datastructures import MultiValueDictKeyError

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def planos(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'cliente_nutricao.html')

def dicas(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'client_treinos.html')
def calendario(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'client_calendar.html')
def progresso(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'client_progresso.html')
def videoaulas(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'client_video.html')

def merch_calcado(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'mercha_calcado.html')

def merch_roupa(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'mercha_roupa.html')

def merch_acessorios(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'mercha_acessorios.html')
def area_cliente(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'client_index.html')

def area_merch(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'mercha_index.html')

def area_suply(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'suply_index.html')

def suply_em(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'suply_emagrecer.html')


def suply_mass(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'suply_massa.html')

def suply_forc(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
     return render(request,'suply_forca.html')




















def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                 login(request, user)
                 user_account = request.user
                 return render(request, 'client/index.html')


            else:
                return render(request, 'client/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'client/login.html', {'error_message': 'Invalid login'})
    return render(request, 'client/login.html')



def create_profile(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = AlbumForm(request.POST or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return render(request, 'client_pessoal.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'client_pessoal.html', context)


def register(request):
    form = UserForm(request.POST or None)
    form_perfil = AlbumForm(request.POST or None)




    if form.is_valid():
        user = form.save(commit=False)
        form_perfil = form.save(commit=False)
        form_perfil.user = request.user

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        form_perfil.save()

        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'client_pessoal.html')
    context = {
        "form": form,
        'form_perfil' :form_perfil

    }
    return render(request, 'register.html', context)




def perfil(request):
    if not request.user.is_authenticated():
        if request.method == "POST":
         try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
         except MultiValueDictKeyError:
             return

         if user is not None:
            if user.is_active:
                    login(request, user)
                    user_account = request.user

                    return render(request,'client_index.html')



            else:
                    return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
         else:
                return render(request, 'login.html', {'error_message': 'Invalid login'})
        return render(request, 'login.html')
    else:
        return render(request,'client_index.html')

from django.shortcuts import render
from django.http import HttpResponse

def index2(request):
    return render(request,'index2.html')
# Create your views here.



def objetivos(request):
    return render(request,'objetivos.html')



def treinos(request):
    return render(request,'treinos.html')


def evolucao(request):
    return render(request,'evolucao.html')

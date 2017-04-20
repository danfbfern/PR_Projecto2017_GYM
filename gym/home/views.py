from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render('../gym/home/temp/index.html')
# Create your views here.

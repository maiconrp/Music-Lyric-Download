from django.shortcuts import render
from django.http import HttpResponse
from Scripts import PesquisarMusica

def index(request):
     return render(request, 'home.html', {})

def pesquisar(request):

    return render(request, 'home.html', {})
# Create your views here


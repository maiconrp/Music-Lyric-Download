from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Scripts import PesquisarMusica
from MusicLyrics.forms import * 
from MusicLyrics.models import * 

def index(request):
     return render(request, 'home.html', {})

def pesquisar(request):
    if request.method == 'POST':
        pesquisa = PesquisaForm(request.POST)

        if pesquisa.is_valid():
            pesquisa.save()

            context = {
                'form'   : pesquisa,
            }
            return render(request, 'home.html', context)
    
    else:
        pesquisa = PesquisaForm()

    context = {
        'form' : pesquisa,
        
    }
    
    return render(request, 'home.html', context)
# Create your views here

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
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
                'form' : pesquisa,
                'musica':result(request, pesquisa)
            }
            return render(request, 'home.html', context)
    else:
        pesquisa = PesquisaForm()

    context = {
        'form' : pesquisa    
    }
    return render(request, 'home.html', context)

def result(request, pesquisa):
    parametros = {
        'art'       : pesquisa.data.get('art'),
        'mus'       : pesquisa.data.get('mus'),
        'apikey'    : pesquisa.data.get('apikey'),
        'extra'     : pesquisa.data.get('extra')
    }
    resposta = requests.get(f"https://api.vagalume.com.br/search.php", params=parametros).json()
    
    if resposta['type'] in ['exact','aprox']:
        return teste_musica(resposta)

    # return preenche_musica(resposta)

def artista(resposta):
    artista = Artista.objects.get_or_create(
        id = resposta['art']['id'], 
        name = resposta['art']['name'], 
        url = resposta['art']['url']

    )[0]
    return artista
    # data = resposta['art']
    # artista = ArtistaForm(data)
    # if artista.is_valid():
    #     artista.save()
    #     print('artista.is_valid()')
    #     return artista

def old_musica(resposta):
    data = resposta['mus'][0]
    pre_musica = MusicaForm(data) 
    
    if pre_musica.is_valid():
        musica = pre_musica.save(commit=False)
        musica.artista = artista(resposta)
        musica.save()
        return musica
    else:
        print(musica.errors)

def musica(resposta):
    data = resposta['mus'][0]
    musica = Musica.objects.get_or_create(
        id = data['id'], 
        name = data['name'], 
        url = data['url'],
        lang = data['lang'],
        text = data['text'],
    )[0]
    musica.artista = artista(resposta)
    musica.save()
    return musica

        
    
    
# Create your views here

# 
# {  'type':'exact',
#    'art':{
#       'id': '3ade68b3g1f86eda3',
#       'name':'Madonna',
#       'url' :'https://www.vagalume.com.br/madonna/'
#    },
#    'mus':[{
#       'id':'3ade68b6g8e27fda3',
#       'name':'Holiday',
#       'lang':2,
#       'url':'https://www.vagalume.com.br/madonna/holiday.html',
#       'text':'Holiday Celebrate\nHoliday Celebrate(..cut..)'
#       'translate':[{
#          'id':'3ade68b6g417afda3',
#          'lang':1,
#          'url':'https://www.vagalume.com.br/madonna/holiday-traducao.html',
#          'text':'[Feriado]\nFeriado, comemore\nFeriado comemore(..cut..)'
#       }]
#    }]
# };

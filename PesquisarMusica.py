import requests
from Download import *
#KEY gerada ao cadastrar na api vagalume
VG_KEY = "9ce9c5e4a931844f8c5f20cb9518e99b" 
TITULOS = BASE_DIR  + "\Titulos.txt"
CAMINHO_MUSICAS = BASE_DIR  + "\Letras\\"

"""# Trecho irrelevante para o código como um todo, apenas para pegar titulos de um arquivo pessoal específico
def pegar_titulos():
    time.sleep(2)
    pg.PAUSE = 0.25
    for i in range(2,10):
        pg.click(x=70, y=723)   #clicar na pagina no arquivo (x=70, y=723)
        pg.write(f'{i}')        #selecionar pag pg.write(i)
        pg.press('enter')       #dar enter pg.press('enter')
        pg.click(x=241, y=478)  #clicar na celula do arquivo 
        pg.hotkey('ctrl', 'c')  #copiar o texto pg.hotkey('crtl', 'c')
        pg.click(x=238, y=757)  #clicar no arquivo txt Point(x=238, y=757)
        pg.hotkey('ctrl', 'v')  #colar pg.hotkey('crtl', 'v')
        pg.hotkey('ctrl', 's')  #salvar o arquivo
        #repete
    else:
        pg.click(x=351, y=753)
        pg.click(x=391, y=753)
        ler_titulos()
"""
def ler_titulos():
    try: 
        with open(f"{TITULOS}", 'r', encoding='utf8') as arquivoTitulos:
            titulos = arquivoTitulos.read().splitlines()
    except:
        print("Não foi possivel abrir o arquivo com os titulos")

    else:
        if titulos:
            for t in titulos:

                t = t.strip().replace(" – ", "-")
                limiter = t.find("-")

                nome = t[:limiter].strip()
                artista = t[limiter+1:].strip()

                musica = buscar_musicas(nome, artista)

                if musica:
                    print(f"{nome} | {artista} - letra encontrada")
                    guardar_musica(musica)
                    pesquisar(nome, artista, *parametro[2:])
                else:
                    print(f"{nome} | {artista} - letra não encontrada")
                    continue
        else:
            print("Não há titulos no arquivo especificado")

def buscar_musicas(nome, artista):
    parametros = {
        'art':artista,
        'mus':nome,
        'apikey':VG_KEY
    }
    print(f"\nPesquisando por: '{nome} - {artista}'")
    try:
        musica = requests.get(f"https://api.vagalume.com.br/search.php", params=parametros).json()
    except:
        print(f"Não foi possivel pesquisar a musica '{nome} - {artista}' ")
    else:
        if musica['type'] in ['exact','aprox']: 
            print(f"\nMusica encontrada com sucesso!!\nLetra disponivel em: \n\t--> {musica['mus'][0]['url']}")  
            guardar_musica(musica)
            pesquisar(nome, artista, *parametro[2:])
            return musica  
          
    return False

def formatar_musica(musica):
    musica_pre_formatada = []
    musica_formatada = []
    index_espacos = []

    musica = musica.replace("\n\n", "\n").split("\n")

    print(f"\nFormatando letra....")

    for linha_da_musica in musica: 
        if len(linha_da_musica) > 28:
            index_espacos = [pos for pos, char in enumerate(linha_da_musica) if char == " "]

            meio = index_espacos[len(index_espacos)//2] 
                       
            index_espacos.clear()
            
            musica_pre_formatada.append(linha_da_musica[:meio]+'\n'+linha_da_musica[meio:])
            #musica_pre_formatada.append(linha_da_musica[meio:])
            continue
        
        musica_pre_formatada.append(linha_da_musica)
        
    for i, linha_da_musica in enumerate(musica_pre_formatada):
        if linha_da_musica and not linha_da_musica.isnumeric():
           
            if i % 2 != 0:
                musica_formatada.append(linha_da_musica + "\n")           
            else:
                musica_formatada.append(linha_da_musica)

    musica_formatada = "\n".join(musica_formatada)
    
    return musica_formatada

def guardar_musica(musica):

    letra = musica['mus'][0]['text']
    nome = musica['mus'][0]['name']
    artista = musica['art']['name']

    musica_formatada = formatar_musica(letra)
    caminho = f"{CAMINHO_MUSICAS}{nome} - {artista}.txt"

    try:
        with open(caminho, 'w', encoding='utf8') as arquivoMusica:
            arquivoMusica.write(musica_formatada)
            print(f"\nLetra salva em: \n\t--> {caminho}")
    except:
        print(f"Não foi possivel guardar essa musica '{nome} - {artista}' ")

tutorial = """
Music and Lyrics Download
Como utilizar: [nome da musica] - [nome do artista] - [modo de audio] [modo de pesquisa]
Ex: "Eu quero ser santo - Eyshila - Playback"

- Parâmetros -
-- Obrigatórios*:
[nome da musica]       Insira aqui o nome da música em si
[nome do artista]      Insira aqui o nome do artista da musica, opcional para baixar a musica, mas essencial para a letra

-- Opcionais:
[modo de audio]        Insira 'Playback' caso queira a música sem a voz. (Padrão: Normal)
[modo de pesquisa]     Insira '-p' para pesquisar usando 'pytube.search' (Padrão: -a : Youtube API)
"""
print(tutorial)

parametro = input("Faça sua pesquisa:").split(" - ")

buscar_musicas(*parametro[0:2])


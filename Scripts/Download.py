import requests
import pytube
import os

YT_KEY = "AIzaSyAOp__h-TG_zyFkg_t9KiaSUQxfim_oF6g"
URL = r"https://www.youtube.com/watch?v="

#c:\Users\User\Documents\Maicon\Programação\Letras-Irmãs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#caracteres especiais que não podem ser usados pra nomear arquivos ou dão algum problema
SPCHAR = r"\/.?*|"

#c:\Users\User\Documents\Maicon\Programação\Letras-Irmãs\Playbacks
CAMINHO_MUS = BASE_DIR + "\Musicas" 

def pesquisar(nome, artista = '', audio = '', modo = '-a'):
    
    pesquisa = f"{nome} - {artista} - {audio}" if audio != '' else f"{nome} - {artista}"
    print(f"\nVerificando arquivos de mídia de '{pesquisa}'")

    parametros = {
        'q': pesquisa, 
        'part':'id', 
        'key': YT_KEY,
        'maxResults':1
        }

    if modo == '-p':
        print(f"Parâmetro de pesquisa\'{modo}\', pesquisando via \'pytube.Search\'...")
        video = pytube.Search(pesquisa)
        videoId = video.results[0].video_id
        
    else:
        video = requests.get("https://www.googleapis.com/youtube/v3/search", params = parametros).json()
        videoId = video["items"][0]["id"]["videoId"]

    if videoId:
        print(f"\nMusica encontrada: {URL + videoId}")
        return baixar(videoId, pesquisa)

    else:
        print(f"\nSem resultados para: '{pesquisa}'")

def baixar(videoId, musica):

    yt = pytube.YouTube(URL+videoId)
   
    #SPCHAR = r"\/.?*|"
    for c in SPCHAR: 
        musica = musica.replace(c, "-") 
    
    video = yt.streams.get_highest_resolution()
    audio = yt.streams.filter(only_audio=True)[-1]

    caminhoMp4 = fr'{CAMINHO_MUS}\Videos\\"{musica}".mp4'
    caminhoMp3 = fr'{CAMINHO_MUS}\Audios\\"{musica}".mp3'

    print("\nRealizando download da música no formato .mp4 (vídeo)...\n")

    try: 
        video.download(output_path = CAMINHO_MUS+"\Videos\\", filename = f"{musica}" + '.mp4') 
        audio.download(output_path = CAMINHO_MUS+"\Audios\\", filename = f"{musica}" + '.mp3')

        print("Download realizado com sucesso!!!")        
        print(f"- Arquivo de Vídeo: {caminhoMp4}")
        print(f"- Arquivo de Áudio: {caminhoMp3}")

    except: 
        print("Ocorreu algum erro ao baixar a música")







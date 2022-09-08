import requests
import pytube
import subprocess
import os

YT_KEY = "AIzaSyAOp__h-TG_zyFkg_t9KiaSUQxfim_oF6g"
URL = r"https://www.youtube.com/watch?v="

#c:\Users\User\Documents\Maicon\Programação\Letras-Irmãs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#caracteres especiais que não podem ser usados pra nomear arquivos ou dão algum problema
SPCHAR = r"\/.?*|"

#c:\Users\User\Documents\Maicon\Programação\Letras-Irmãs\Playbacks
CAMINHO_PB = BASE_DIR + "\Playbacks" 

def pesquisar(nome, artista = '', audio = '', modo = '-a'):
    
    pesquisa = f"{nome} - {artista} - {audio}"
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
        print(f"\nMusica encontrada!! \nUrl: {URL + videoId} \nID: {videoId}")
        return baixar(videoId, pesquisa)

    else:
        print(f"\nSem resultados para: '{pesquisa}'")

def baixar(videoId, musica):

    yt = pytube.YouTube(URL+videoId)
   
    #SPCHAR = r"\/.?*|"
    for c in SPCHAR: 
        musica = musica.replace(c, "-") 
    
    video = yt.streams.get_highest_resolution()

    caminhoMp4 = fr'{CAMINHO_PB}\Videos\\"{musica}".mp4'
    caminhoFlac = fr'{CAMINHO_PB}\Musicas\\"{musica}".flac'

    print("Realizando download da música no formato .mp4 (vídeo)...")

    try: 
        video.download(output_path = CAMINHO_PB+"\Videos\\", filename = f"{musica}" + '.mp4')             
        print(f"Download realizado com sucesso!!!\n - video salvo em:\n\t-->  {caminhoMp4}")

    except: 
        print("Ocorreu algum erro ao baixar a música")

    else: 
        return converter(caminhoMp4, caminhoFlac)

def converter(caminhoMp4, caminhoFlac):
    print("Convertendo o arquivo...")  

    ffmpeg = (f"ffmpeg -i  {caminhoMp4} -b:v 320k -vn -ar 48000 -acodec flac -ac 2 -ab 320k -f flac {caminhoFlac} -y -stats -loglevel quiet")

    try: 
        subprocess.run(
            ffmpeg, 
            shell=True, 
            encoding='utf8',
            )

        print(f"Arquivo convertido salvo em:\n\t--> {caminhoFlac}")

    except: 
        print("Erro ao converter o arquivo")




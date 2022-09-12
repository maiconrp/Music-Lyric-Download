# Music Lyric Download
[![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento%20-green?style=for-the-badge)](https://github.com/maicon15rp/Music-Lyric-Download)
[![GitHub issues](https://img.shields.io/github/issues/maicon15rp/Music-Lyric-Download?style=for-the-badge)](https://github.com/maicon15rp/Music-Lyric-Download/issues)
[![GitHub stars](https://img.shields.io/github/stars/maicon15rp/Music-Lyric-Download?style=for-the-badge)](https://github.com/maicon15rp/Music-Lyric-Download/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/maicon15rp/Music-Lyric-Download?style=for-the-badge)](https://github.com/maicon15rp/Music-Lyric-Download/network)

## Índice 

* [Descrição do projeto](#descri%C3%A7%C3%A3o-do-projeto)
* [Como funciona?](#como-funciona)
* [Funcionalidades](#funcionalidades-hammer_and_wrench)
* [Layout](#layout-computer)
* [Linguagens, dependencias e pré-requisitos](#linguagens-dependencias-e-pr%C3%A9-requisitosbooks)
* [APIS Utilizadas](#apis-utilizadas)
* [Como rodar o programa](#como-rodar-o-programa-arrow_forward)
* [Tarefas em aberto](#tarefas-em-aberto-hourglass_flowing_sand)

## Descrição do projeto 

<p align="justify">
  Uma ferramenta em python para download de músicas de forma automatizada. Ao fornecer o nome da música + artista, o programa retorna a música em vídeo, audio e a letra formatada para projeção.
</p>

## Como funciona?
O usuário insere o nome da música + artista que deseja baixar. Com esses dados, é enviada uma requisição de pesquisa para a API do YouTube, na qual seu retorno é convertido em um json com informações dos vídeos encontrados. Após isso, é 

## Funcionalidades :hammer_and_wrench:

:heavy_check_mark: Download de músicas e vídeos do YouTube + playback's

:heavy_check_mark: Pesquisa e formatação de Letras

:heavy_check_mark: Conversão de video pra audio

:heavy_check_mark: Download em massa

## Layout :computer:
> :construction: Projeto em construção, interface ainda em desenvolvimento.

#### Protótipos
:computer: [Desktop](https://www.figma.com/proto/8U3c7uuIjSA8DCGzYZazVC/Music-and-Lyric?node-id=10%3A219&scaling=scale-down&page-id=10%3A218)
:iphone: [Mobile](https://www.figma.com/proto/8U3c7uuIjSA8DCGzYZazVC/Music-and-Lyric?node-id=1%3A2&scaling=scale-down&page-id=0%3A1)

:dart: Pretende-se desenvolvê-la com [Flet](https://flet.dev/) ou [Django](https://docs.djangoproject.com/en/4.0/)

## Linguagens, dependencias e pré-requisitos:books:
:warning: [Python 3](https://www.python.org/downloads/)
#### Libs Nativas:
:warning: [Subprocess](https://docs.python.org/3/library/subprocess.html)

:warning: [OS](https://docs.python.org/3/library/os.html)

:warning: [TQDM](https://tqdm.github.io/)
#### Libs de Terceiros
:warning: [Python Requests](https://requests.readthedocs.io/en/latest/)

:warning: [Pytube](https://pytube.io/en/latest/)

#### Outros:
:warning: [ffmpeg](https://ffmpeg.org/)* 

*Será substituída posteriormente

Veja como instalar essas dependências [aqui](#como-rodar-o-programa-arrow_forward)

## API's Utilizadas
:globe_with_meridians: [Youtube API](https://developers.google.com/youtube/?hl=pt_BR)

:globe_with_meridians: [Vagalume API](https://api.vagalume.com.br/docs/)

## Como rodar o programa :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/maicon15rp/Music-Lyric-Download.git
```

Sua pasta estará assim:
```
Music-Lyric-Download
└─── __pycache__
└─── .gitignore
└─── Download.py
└─── FormatarHarpa.py
└─── PesquisarMusica.py
└─── README.md
└─── requirements.txt
```

Dentro de `Music-Lyric-Download`,  execute:
```
pip install -r requirements.txt
```

:warning: Além disso, instale o ffmpeg seguindo estes tutoriais: [Windows](https://pt.wikihow.com/Instalar-o-FFmpeg-no-Windows) | [Linux](https://www.hostinger.com.br/tutoriais/como-instalar-ffmpeg)


Em  seguida, execute o arquivo `PesquisarMusica.py` com o comando*: 
:open_file_folder:
```
py PesquisarMusica.py
```
*Em alguns casos, o comando pode variar: `python PesquisarMusica.py`, `python3 PesquisarMusica.py`, `py3 PesquisarMusica.py`

Você receberá a seguinte mensagem:

```
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

Faça sua pesquisa:
```

Faça sua pesquisa conforme o cabeçalho acima.

:ballot_box_with_check:Se tudo ocorrer bem, a música será baixada e armazenada na pasta "Playbacks", sua pasta ficará assim: :open_file_folder:
```
Music-Lyric-Download
└─── Letras
└─── Playbacks
      └─── Audios
      └─── Videos     
└─── __pycache__
└─── .gitignore
└─── Download.py
└─── FormatarHarpa.py
└─── PesquisarMusica.py
└─── README.md
```

Onde a letra é armazenada na pasta `Letras`, a música nas subpastas `Audios` e `Videos`

## Resolvendo Problemas :exclamation:

Em [issues](https://github.com/maicon15rp/Music-Lyric-Download/issues) temos a resolução de alguns problemas que foram abertos e ocorreram ou estão ocorrendo durante o desenvolvimento desse projeto. 

## Tarefas em aberto :hourglass_flowing_sand:

Algumas funcionalidades ainda precisam ser melhoradas e ajustadas, tais quais, giram em torno de:

:memo: Desenvolver a interface para promover uma melhor experiencia de uso do programa.

:memo: Ajustar e refatorar trechos do Código para melhor legibilidade e desempenho.

:memo: Implementar [Alinhamento Forçado](https://linguistics.berkeley.edu/plab/guestwiki/index.php?title=Forced_alignment#:~:text=Forced%20alignment%20refers%20to%20the,automatically%20generate%20phone%20level%20segmentation.) da música com a letra para criar projeções automáticas.

:memo: Adaptar a entrada de musicas em massa com a função que as receberia

:memo: Permitir que o usuário escolhar baixar audio, vídeo ou letra individualmente

:memo: Opção de baixar musica e sua versão playback juntas

:memo: Trocar execução do ffmmpg usando subprocess por lib `ffmpeg-python`

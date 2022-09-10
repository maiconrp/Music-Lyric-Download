# Music Lyric Download
![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento%20-green)

## Índice 

* [Descrição do projeto](https://github.com/maicon15rp/Music-Lyric-Download#descri%C3%A7%C3%A3o-do-projeto)
* [Como funciona?](https://github.com/maicon15rp/Music-Lyric-Download#como-funciona)
* [Funcionalidades](https://github.com/maicon15rp/Music-Lyric-Download#funcionalidades-hammer_and_wrench)
* [Layout](https://github.com/maicon15rp/Music-Lyric-Download#layout-computer)
* [Linguagens, dependencias e pré-requisitos](https://github.com/maicon15rp/Music-Lyric-Download#linguagens-dependencias-e-pr%C3%A9-requisitosbooks)
* [APIS Utilizadas](https://github.com/maicon15rp/Music-Lyric-Download#apis-utilizadas)
* [Como rodar o programa](https://github.com/maicon15rp/Music-Lyric-Download#como-rodar-o-programa-arrow_forward)
* [Tarefas em aberto](https://github.com/maicon15rp/Music-Lyric-Download#tarefas-em-aberto-hourglass_flowing_sand)

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
:construction: Projeto em construção ainda sem interface.:construction: :hourglass_flowing_sand:

:dart: Pretende-se desenvolvê-la com <a href="https://flet.dev/">Flet</a> ou  <a href="https://docs.djangoproject.com/en/4.0/">Django</a>

## Linguagens, dependencias e pré-requisitos:books:
:warning: [Python 3](https://www.python.org/downloads/)

:warning: [Python Requests](https://requests.readthedocs.io/en/latest/)

:warning: [Pytube](https://pytube.io/en/latest/)

:warning: [Subprocess](https://docs.python.org/3/library/subprocess.html)

:warning: [OS](https://docs.python.org/3/library/os.html)

:warning: [TQDM](https://tqdm.github.io/)

## API's Utilizadas
:globe_with_meridians: [Youtube API](https://developers.google.com/youtube/?hl=pt_BR)

:globe_with_meridians: [Vagalume API](https://api.vagalume.com.br/docs/)

## Como rodar o programa :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/maicon15rp/Music-Lyric-Download
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
```

Em  seguida, execute o seguinte arquivo: 
:open_file_folder:
```
Music-Lyric-Download
└─── PesquisarMusica.py
```
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

## Tarefas em aberto :hourglass_flowing_sand:

Algumas funcionalidades ainda precisam ser melhoradas e ajustadas, tais quais, giram em torno de:

:memo: Desenvolver a interface para promover uma melhor experiencia de uso do programa.

:memo: Ajustar e refatorar trechos do Código para melhor legibilidade e desempenho.

:memo: Implementar [Alinhamento Forçado](https://linguistics.berkeley.edu/plab/guestwiki/index.php?title=Forced_alignment#:~:text=Forced%20alignment%20refers%20to%20the,automatically%20generate%20phone%20level%20segmentation.) da música com a letra para criar projeções automáticas.
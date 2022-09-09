from PesquisarMusica import formatar_musica
from tqdm import tqdm

def receber_caminhos():
    hinos = []
    while True:
        hino = input()
        if hino:
            hinos.append(hino.replace('"', ""))
        else:
            break
    abrir_arquivos(hinos)

def receber_txt():
    hinos = []
    #txtCaminhos = input("Informe o caminho do txt: ")
    txtCaminhos = r"C:\Users\User\Documents\Maicon\Programação\Letras-Irmãs\Testes\CaminhoHarpa.txt"

    with open(txtCaminhos, 'r', encoding='utf8') as txt:
        hinos = txt.read().splitlines()
       
    abrir_arquivos(hinos)

def abrir_arquivos(arquivos):
    for caminho in tqdm(arquivos):
        caminho = caminho.replace('"', "")
        with open(caminho, 'r') as arquivo_hino:
            letra = arquivo_hino.read().splitlines()

        letra = formatar_harpa(letra)

        with open(caminho, 'w') as arquivo_hino:
            arquivo_hino.write(letra)


def formatar_harpa(letra):
    letra_formatada = []
    refrao = []
    espaco = 0

    for linha_refrao in letra:
        if linha_refrao.isupper():
            refrao.append(linha_refrao)
    refrao = quebrar_linhas(refrao)
    for linha in letra:
        if linha:
            letra_formatada.append(linha)
        else:
            espaco += 1
            if espaco > 2:
                letra_formatada.extend(refrao)

    letra_formatada = "\n".join(letra_formatada)

    return formatar_musica(letra_formatada)

def quebrar_linhas(refrao):
    musica_pre_formatada = []
    index_espacos = []
    for linha in refrao: 
            if (linha.isupper and len(linha)> 22) or (len(linha)> 28):
                index_espacos = [pos for pos, char in enumerate(linha) if char == " "]

                meio = index_espacos[len(index_espacos)//2] 
                        
                index_espacos.clear()
                
                musica_pre_formatada.append(linha[:meio])
                musica_pre_formatada.append(linha[meio:])
                continue
            
            musica_pre_formatada.append(linha)
    
    return musica_pre_formatada

receber_caminhos()

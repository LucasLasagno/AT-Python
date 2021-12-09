import os

dir = input('Digite o diretório: ')
arch = input('Digite o nome do arquivo: ')


def abre_arq():
    try:
        os.startfile(os.path.join(dir, arch))
        print(f'{arch} foi aberto!')
    except Exception:
        print('Não foi possível abrir o arquivo!')


abre_arq()
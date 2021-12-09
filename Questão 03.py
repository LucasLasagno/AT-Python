from psutil._common import bytes2human
import os

arch = []
dir = input('Digite o caminho de um diretório: ')
os.chdir(dir)
list_dir = os.listdir(os.chdir(dir))


def leitura_dir():
    for i in list_dir:
        if os.path.isfile(os.path.join(dir, i)):
            arch.append({'name': i,
                'size': os.stat(os.path.join(dir, i)).st_size})

            arch.sort(key=lambda x: x['size'], reverse=True)

    with open('VALORES DA ESTRUTURA EM ORDEM.txt', 'w') as arquivo:
        arquivo.write(str(arch))


def result():
    print('{} {:<10} {:^10}'.format(' '*2, 'Tamanho', 'Arquivo'), sep="\n")
    for arquivo in arch:
        print('{} {:<10} {:^10}'.format(
            ' '*2, bytes2human(arquivo['size']), arquivo['name']))
    print('\nO arquivo gerado se encontra no diretório especificado.')


leitura_dir()
resultado()
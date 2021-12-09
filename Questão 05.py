lista_a = []
lista_b = []
total = []

def leitura_arq():
    try:
        with open('a.txt', 'r') as txt_a:
            for i in txt_a.readlines():
                txt_a = i.split(' ')
        for numero in txt_a:
            lista_a.append(int(numero))

        with open('b.txt', 'r') as txt_b:
            for i in txt_b.readlines():
                txt_b = i.split(' ')
        for numero in txt_b:
            lista_b.append(int(numero))
    except Exception:
        print('O arquivo não foi encontrado')


def verifica():
    tam_a = len(lista_a)
    tam_b = len(lista_b)
    dif = tam_a - tam_b

    if dif > 0:
        for i in range(0, abs(dif)):
            lista_b.append(0)
    elif dif < 0:
        for i in range(0, abs(dif)):
            lista_a.append(0)
    else:
        pass
    for a, b in zip(lista_a, lista_b):
        total.append(sum([a, b]))

def result():
    for soma in total:
        print('{}{:<7}'.format(' '*2, soma))


leitura_arq()
verifica()
result()
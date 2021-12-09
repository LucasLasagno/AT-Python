import multiprocessing
import time
import random

vet_b = []

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def calcula_fatorial(num1, num2):
    fat_lista = num1.get()
    vetores = []
    for item in fat_lista:
        fat = fatorial(item)
        vetores.append(fat)
    num2.put(vetores)


if __name__ == '__main__':
    t_vetor = int(input('Tamanho do vetor: '))
    inicio_tempo = float(time.time())

    vet_a = []
    for i in range(t_vetor):
        vet_a.append(random.randint(0, 20))

    n_processamento = 4

    fila = multiprocessing.Queue()
    fora_fila = multiprocessing.Queue()

    lista_processo = []
    for i in range(num_processamento):
        inicio = i * int(t_vetor/n_processamento)
        fim = (i + 1) * int(t_vetor/n_processamento)
        fila.put(vet_a[inicio:fim])
        multip = multiprocessing.Process(target=calcula_fatorial, args=(fila,
                                                           fora_fila))
        multip.start()
        lista_processo.append(multip)

    for multip in lista_processo:
        multip.join()

    fim_tempo = float(time.time())

    tempo = fim_tempo - inicio_tempo

    print(f'Tempo de multi-processamento: {tempo}')
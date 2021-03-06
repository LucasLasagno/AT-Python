import random
import time
import threading

tam_vetor = int(input('Tamanho do vetor: '))
vet_a = []
vet_b = []
lista_thread = []
n_thread = 4

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def calcula_fatorial_thread(lista_a, inicio, fim):
    for item in lista_a[inicio:fim]:
        fat = fatorial(item)
        vet_b.append(fat)

def thread_task():
    inicio_tempo = float(time.time())

    for i in range(tam_vetor):
        vet_a.append(random.randint(0, tam_vetor))

    list_size = len(vet_a)

    for i in range(num_thread):
        inicio = i * int(list_size/num_thread)
        fim = (i + 1) * int(list_size/num_thread)
        t = threading.Thread(target=calcula_fatorial_thread, args=(vet_a, inicio, fim))
        t.start()
        lista_thread.append(t)

    for t in lista_thread:
        t.join()

    fim_tempo = float(time.time())

    resultado = fim_tempo - inicio_tempo

    return resultado


tempo = thread_task()

print(f'Tempo de multi thread: {tempo}')
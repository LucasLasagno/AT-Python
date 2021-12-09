import time
import random

t_vetor = int(input('Tamanho do vetor: '))
vet_a = []
vet_b = []

def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return (fat)

def tempo_calculo():

    inicio = float(time.time())

    for i in range(tam_vetor):
        vet_a.append(random.randint(0, tam_vetor))

    for item in vetor_a:
        seq = fatorial(item)
        vetor_b.append(seq)
    fim = float(time.time())
    
    resultado = fim - inicio

    return resultado

tempo = tempo_calculo()
print(f'Tempo de processamento: {tempo}')
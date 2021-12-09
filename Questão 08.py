vet_A = [8, 13]
vet_B = []

def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)

def resultado():
    for i in vet_A:
        resultado_fatoracao = fatorial(i)
        vet_B.append(resultado_fatoracao)

    print(vet_B)


resultado()
def soma_h(x):
    soma = 0
    for e in range(1, x+1):
        inverso = (1/e)
        soma += inverso
    return round(soma,2)
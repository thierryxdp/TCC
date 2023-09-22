def fatorial(N):
    contador = 0
    numeros = N
    fatorial = 1
    while numeros[contador] > 2:
        fatorial = (fatorial)*(numeros - 1)
        contador = contador + 1
    return fatorial
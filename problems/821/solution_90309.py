def fatorial(N):
    contador = 0
    numeros = N
    fatorial = 1
    while numeros[contador] > int(1):
        fatorial = (fatorial)*(numeros - 1)
        contador = contador + 1
    return fatorial
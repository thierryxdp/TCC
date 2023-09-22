def fatorial(N):
    contador = 0
    fatorial = 1
    while N[contador] > 1:
        fatorial = fatorial * N[contador]
        contador = contador + 1
    return fatorial
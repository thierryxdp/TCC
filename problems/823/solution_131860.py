def faltante(lista):
    N = max(lista)
    for numero in range(1,N):
        if numero not in lista:
            return numero
    return N+1
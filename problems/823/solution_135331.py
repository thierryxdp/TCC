def faltante(lista):
    N=1
    i=0
    while N<len(lista):
        if N not in lista:
            i=i+N
    return i
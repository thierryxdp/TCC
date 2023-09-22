def faltante(lista):
    N=1
    while N<len(lista):
        if N not in lista:
            return N
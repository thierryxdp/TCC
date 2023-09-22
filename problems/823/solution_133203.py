def faltante(lista):
    """Dada uma lista com N − 1 inteiros numerados de 1 a N, descubre qual número
    inteiro desse intervalo esta faltando"""
    """list -> int"""
    
    i = 0
    listacerta = list(range(1,len(lista)+2))
    while i < len(lista):
        if lista[i] != listacerta[i]:
            return i + 1
        if lista[-1] != listacerta[-1]:
            return listacerta[-1]
        i = i + 1
def faltante (lista):
    """recebe uma lista com N − 1 inteiros numerados de 1 a N e retorna qual numero
inteiro deste intervalo esta faltando"""
    i=0
    lista.sort()
    while i < len(lista):
        if lista[i]-1 not in lista and lista[i]-1 != 0:
            return lista[i]-1
        i += 1
    return lista[-1]+1
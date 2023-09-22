def faltante(lista):
    '''ao receber uma lista de números inteiros numerados
    de 1 ao último número, retorna o número que falta da
    lista.
    list -> int'''
    i = 1
    while i in lista:
        i = i + 1
    return i
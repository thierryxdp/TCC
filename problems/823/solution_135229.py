def faltante(lista):
    '''dada uma lista de números inteiros numerados
    de 1 ao último número, retorna o número que falta da
    lista.
    list -> int'''
    num = 1
    while num in lista:
        num = num + 1
    return num
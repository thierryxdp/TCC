def faltante (lista):
    '''Dada uma lista com N-1 inteiros numerados de 1 a N, retorna o número que
    falta neste intervalo.
    list -> int'''
    list.sort (lista)
    contador = 2
    while 1 in lista and len(lista)<lista[-1]:
        if contador not in lista:
            return contador
        contador = contador + 1
    if 1 not in lista:
        return 1
    if 1 in lista and len(lista) in lista:
        return len(lista) + 1
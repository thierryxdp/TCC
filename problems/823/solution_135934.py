def faltante(lista):
    """dada uma lista com N-1 inteiros numerados de 1 a N,retorna o número que falta.
    list->int"""
    list.sort(lista)
    i=0
    while i<=len(lista):
        if lista[1] not in lista:
            return lista[i]
        i=i+1
    return lista[-1]+1
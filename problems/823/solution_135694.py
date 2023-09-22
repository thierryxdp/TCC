def faltante(lista):
    """dada uma lista com N-1 inteiros numerados de 1 a N,retorna o número que falta.
    list->int"""
    list.sort(lista)
    i=0
    n=0
    while lista[i]<len(lista):
        if n in lista:
            n+1
        i=i+1
    return n
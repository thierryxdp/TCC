def faltante(lista):
    """dada uma lista com N-1 inteiros numerados de 1 a N,retorna o número que falta.
    list->int"""
    list.sort(lista)
    i=0
    n=0
    while lista[i+1]-lista[i]==1 and lista[i]!=lista[-1]:
        if n in lista:
            i=i+1
        n=n+1
    return n+1
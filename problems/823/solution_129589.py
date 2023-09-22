def faltante(lista):
    '''Dada uma lista de n-1 números inteiros numerados de 1 a n, descobre qual número está faltando'''
    '''list->int'''
    list.sort(lista)
    x=1
    falta
    while x<len(lista):
        if lista[x]-lista[x-1]>1:
            falta=lista[x]-1
        else:
            x=x+1
    return falta
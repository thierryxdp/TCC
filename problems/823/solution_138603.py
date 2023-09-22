def faltante(lista=[]):
    '''função que dada uma lista com
    n-1 inteiros numerados de 1 a n,
    descobre qual inteiro do intervalo
    está faltando
    lista -> int'''
    
    lista.sort()
    for i in range(len(lista)):
        if lista[i]!=i+1:
            return i+1
    return 0
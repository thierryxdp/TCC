def faltante(lista):
    '''faltante recebe uma lista com N-1 inteiros numerados de 1 a N e devolve o número inteiro que está faltando no intervalo.
    list-->int.'''
    i=0
    n=(len(lista))+1
    falta=(range(1,n))
    while i<len(lista):
        if lista[i] in falta:
            list.remove(falta,lista[i])
        i=i+1
    return falta
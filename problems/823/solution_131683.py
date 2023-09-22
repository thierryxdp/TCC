def faltante(lista):
    '''Dada uma lista com N - 1 inteiros descubra qual número inteiro deste intervalo está faltando'''
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1]<len(lista)+1:
        return len(lista)+1
    c=0
    falta=0
    while c<len(lista)-1:
        if lista[c+1]-lista[c]>1:
            falta=falta+lista[c]+1
        c=c+1
    return falta
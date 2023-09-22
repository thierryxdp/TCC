def faltante(lista):
    '''Dada uma lista de tamanho n-1 contendo números
    inteiros (não repetidos) de 1 a n, retorna o número
    inteiro x que pertence ao intervalo [1,n], mas que não
    pertence a lista de entrada.
    list -> int'''
    
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1]<len(lista)+1:
        return len(lista)+1
    i = 0
    falta = 0
    while i < len(lista)-1:
        if lista[i+1]-lista[i]>1:
            falta=falta+lista[i]+1
        i = i + 1
    return falta
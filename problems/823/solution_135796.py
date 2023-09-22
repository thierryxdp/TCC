def faltante(lista):
    '''
       função que, dada uma lista com n-1 inteiros numerados 
       de 1 a n, retorna qual numero inteiro deste intervalo
       esta faltando
       list -> int
    '''
    i = 0
    retorno = 1
    lista.sort()
    if len(lista) == lista[-1]:
        retorno = len(lista) + 1
    while i<(len(lista)-1):
        if (lista[i]+1) != lista[i+1]:
            retorno = lista[i]+1
        i=i+1
    return retorno
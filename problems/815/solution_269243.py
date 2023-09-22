def insere(lista_numero,n):
    '''
    dado uma lista de numero e um numero inteiro n, retorna
    a lista ordenada incluindo o numero n nela
    '''
    x=list.sort(lista_numero+[n])
    return x
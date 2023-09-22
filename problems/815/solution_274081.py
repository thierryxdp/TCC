def insere(lista_numero,n):
    '''Recebe uma lista ordenada de numeros inteiros
    e um numero inteiro n e insere n na posição correta'''
    lista_numero  += [n]
    return sorted(lista_numero)
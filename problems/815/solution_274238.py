def insere(lista_numero,n):
    '''Função que dada uma lista ordenada (crescente) de números inteiros e um número n, inclui n na posição correta, ou seja, de tal maneira que a lista continue ordenada'''
    L=lista_numero+n
    return list.sort(L)
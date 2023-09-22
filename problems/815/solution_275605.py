def insere (lista_numero, n):
    '''Insere numa lista ordenada (1ª entrada) um número n (2ª entrada) de tal forma que a lista continue ordenada.'''
    n = str (n)
    n = list (n)
    lista = lista_numero + n
    return sorted (lista)
def insere(lista_numero, n):
    '''Dada uma lista e um numero n, insere o numero n na lista em orddem crescente.
    lista, Int->'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero
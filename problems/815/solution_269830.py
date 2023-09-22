def insere(lista, n):
    '''Entre com uma lista e um nummero para ser acrescentado na lista mantendo a
    ordem
    Lista, Int -> Lista'''
    
    Nlista = lista.insert(-1, n)

    return Nlista.sort()
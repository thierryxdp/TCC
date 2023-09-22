def insere(lista, n):
    '''Entre com uma lista e um nummero para ser acrescentado na lista mantendo a
    ordem
    Lista, Int -> Lista'''
    
    Nlista = lista
    Nlista = Nlista.insert(-1, n)
    Nlista2 = Nlista.sort()

    return Nlista2
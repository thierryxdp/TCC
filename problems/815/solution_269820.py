def insere(lista, n):
    '''Entre com uma lista e um nummero para ser acrescentado na lista mantendo a
    ordem
    Lista, Int -> Lista'''
    lista = lista.insert(n)
    Nlista = lista.sort(lista)

    return Nlista
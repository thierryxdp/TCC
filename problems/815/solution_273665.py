def insere(lista_numero,n):
    ''' Essa função recebe uma lista de numero e coloca ela na possiççao correta
    '''
    lista_numero.insert(0,n)
    list.sort(lista_numero)
    return lista_numero
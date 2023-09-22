def insere(lista_numero, n):
    ''' função que retorna uma lista de ordem crescente com números inteiros.
    list(int) -> list
    '''
    list.insert(0, n)
    list.sort(lista_numero)
    return lista_numero
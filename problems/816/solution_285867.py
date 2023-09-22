def maiores(lista_numeros, n):
    ''' função que dada uma lista, retorna outra lista contendo todos os números maiores que N em ordem crescente.
    list(int) -> list
    '''
    list.insert(lista_numeros, 0, n)
    list.sort(lista_numeros)
    lista1 = lista_numeros[list.index(lista_numeros, n) + 1:]
    return lista1
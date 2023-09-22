def insere(lista_numero, n):
    '''Dado um lista de numeros e um número, ela adiciona o número a lista;list, float => list'''
    lista_com_n = lista_numero + [n]
    list.sort(lista_com_n)
    return lista_com_n
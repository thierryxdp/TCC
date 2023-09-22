def insere(lista_numero, n):
    '''Dada uma lista ordenada de números insere o número n
    de forma a manter a sequência ordenada.
    list, int ->list'''
    lista = lista_numero+[n]
    list.sort (lista)
    return lista
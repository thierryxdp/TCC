def insere(lista, n):
    '''Função que posiciona corretamente um número n em uma lista'''
    lista = lista + [n]
    lista = list.sort(lista)
    return lista
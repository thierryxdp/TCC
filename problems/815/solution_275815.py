def insere(lista, n):
    '''Função que posiciona corretamente um número n em uma lista'''
    lista = lista + [n]
    return list.sort(lista)
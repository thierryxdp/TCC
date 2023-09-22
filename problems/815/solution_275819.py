def insere(lista_numero, n):
    '''Função que posiciona corretamente um número n em uma lista'''
    lista = lista_numero + [n]
    l = list.sort(lista)
    return l
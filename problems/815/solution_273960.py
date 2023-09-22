def insere(lista_numero, n):
    '''função que insere um numero n de forma ordenada numa lista
    lista, float -> lista'''
    lista_numero = lista_numero + [n] 
    list.sort(lista_numero)
    return lista_numero
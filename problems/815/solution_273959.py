def insere(lista_numero, n):
    '''função que insere um numero n de forma ordenada numa lista
    lista, float -> lista'''
    lista_numero = lista_numero + [n] 
    return list.sort(lista_numero)
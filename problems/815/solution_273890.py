def insere(lista_numero,n):
    '''Insere um numero em uma lista ordenada'''
    lista = lista_numero + [n]
    resultado=sorted(lista)
    return resultado
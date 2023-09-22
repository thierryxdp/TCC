def insere(lista_numero, n):
    ''' funcao que insere n na lista ordenada
list, int -> list|| None'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero
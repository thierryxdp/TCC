def insere(lista_numero, n):
    '''insere um numero n na lista e depois a reorganiza.
    list->list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero
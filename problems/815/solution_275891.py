def insere(lista_numero, n):
    '''Insere um número n em ordem crescente em uma lista
        list int --> list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero
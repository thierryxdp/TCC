def insere(lista_numero,n):
    '''Função que insere um n numa lista
    list, int -> list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista
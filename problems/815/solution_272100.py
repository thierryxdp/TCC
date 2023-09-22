def insere(lista_numero,n):
    '''Retorna a lista de entrada mais o valor (n), em ordem
    crescente
    list, int -> list '''
    lista_numero = lista_numero + [n]
    lista_numero.sort()
    return lista_numero